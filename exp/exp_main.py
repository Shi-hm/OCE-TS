import logging
from data_provider.data_factory import data_provider
from exp.exp_basic import Exp_Basic
from loss.OrdinalCrossEntropyLoss import OrderedCrossEntropyLoss
from loss.hl_gauss import HLGaussLossFromSupport
from models import DLinear, Linear, NLinear
from utilss.tools import EarlyStopping, visual, adjust_learning_rate
from utilss.metrics import metric
import numpy as np
import pandas as pd
import torch
from torch import optim
import os
import time

import warnings
warnings.filterwarnings('ignore')

def Mseloss(outputs, batch_y):
    return torch.mean((outputs - batch_y) ** 2)

def count_parameters(model):
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Total parameters: {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")

def add_gaussian_noise_with_snr(batch_x, snr_db, seed=None):
    x_np = batch_x.detach().cpu().numpy()
    signal_power = np.mean(x_np ** 2)
    snr_linear = 10 ** (snr_db / 10)
    noise_power = signal_power / snr_linear
    rng = np.random.default_rng(seed=seed)
    noise = rng.normal(loc=0, scale=np.sqrt(noise_power), size=x_np.shape)
    noisy_x = x_np + noise
    return torch.tensor(noisy_x, dtype=batch_x.dtype, device=batch_x.device)

class Exp_Main(Exp_Basic):
    def __init__(self, args):
        super(Exp_Main, self).__init__(args)
        self.num_bins = args.num_bins
        self.support = torch.linspace(-1, 1, self.num_bins + 1).to(self.device)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.sigma = args.sigma

    def _build_model(self):
        model_dict = {
            'DLinear': DLinear,
            'NLinear': NLinear,
            'Linear': Linear,
        }
        model = model_dict[self.args.model].Model(self.args).float()
        count_parameters(model)
        return model

    def _get_data(self, flag):
        data_set, data_loader = data_provider(self.args, flag)
        return data_set, data_loader

    def _select_optimizer(self):
        model_optim = optim.Adam(self.model.parameters(), lr=self.args.learning_rate)
        return model_optim

    def _select_criterion(self):
        return OrderedCrossEntropyLoss()

    def vali(self, vali_loader, criterion):
        self.model.eval()
        total_loss = []
        criterion = self._select_criterion()

        hlg_loss = HLGaussLossFromSupport(self.support, sigma=self.sigma).to(self.device)

        with torch.no_grad():
            for i, (batch_x, batch_y) in enumerate(vali_loader):
                batch_x = batch_x.float().to(self.device)
                batch_y = batch_y.float().to(self.device)
                eps = 1e-8
                min_val = batch_y.min(axis=1, keepdims=True).values
                max_val = batch_y.max(axis=1, keepdims=True).values

                batch_y_norm = 2 * (batch_y - min_val) / (max_val - min_val + eps) - 1
                target_probs = hlg_loss.transform_to_probs(batch_y_norm)
                # (0, 1)
                # batch_y_norm = (batch_y - min_val) / (max_val - min_val + eps)
                # target_probs = hlg_loss.transform_to_probs(batch_y_norm)

                min_val = batch_x.min(axis=1, keepdims=True).values
                max_val = batch_x.max(axis=1, keepdims=True).values
                batch_x_norm = 2 * (batch_x - min_val) / (max_val - min_val + eps) - 1
                # (0, 1)
                # batch_x_norm = (batch_x - min_val) / (max_val - min_val + eps)

                # batch_x_noisy = add_gaussian_noise_with_snr(batch_x_norm, snr_db=20, seed=i)
                # outputs = self.model(batch_x_noisy)

                outputs = self.model(batch_x_norm)
                f_dim = -1 if self.args.features == 'MS' else 0
                outputs = outputs[:, -self.args.pred_len:, f_dim:]
                target_probs = target_probs[:, -self.args.pred_len:, f_dim:]

                loss = criterion(outputs, target_probs)
                total_loss.append(loss.unsqueeze(0))
        return torch.cat(total_loss).mean().item()

    def train(self, setting,scheduler=None):
        train_data, train_loader = self._get_data(flag='train')
        vali_data, vali_loader = self._get_data(flag='val')

        path = os.path.join(self.args.checkpoints, setting)
        if not os.path.exists(path):
            os.makedirs(path)

        time_now = time.time()

        train_steps = len(train_loader)
        early_stopping = EarlyStopping(patience=self.args.patience, verbose=True)

        model_optim = self._select_optimizer()
        criterion = self._select_criterion()

        hlg_loss = HLGaussLossFromSupport(self.support, sigma=self.sigma).to(self.device)

        print(">>> Start Training")

        for epoch in range(self.args.train_epochs):
            iter_count = 0
            train_loss = []

            self.model.train()
            epoch_time = time.time()

            for i, (batch_x, batch_y) in enumerate(train_loader):
                iter_count += 1
                model_optim.zero_grad()
                batch_x = batch_x.float().to(self.device)
                batch_y = batch_y.float().to(self.device)

                eps = 1e-8
                min_val = batch_y.min(axis=1, keepdims=True).values
                max_val = batch_y.max(axis=1, keepdims=True).values
                batch_y_norm = 2 * (batch_y - min_val) / (max_val - min_val + eps) - 1

                target_probs = hlg_loss.transform_to_probs(batch_y_norm)

                # (0, 1)
                # batch_y_norm = (batch_y - min_val) / (max_val - min_val + eps)
                # target_probs = hlg_loss.transform_to_probs(batch_y_norm)

                min_val = batch_x.min(axis=1, keepdims=True).values
                max_val = batch_x.max(axis=1, keepdims=True).values
                batch_x_norm = 2 * (batch_x - min_val) / (max_val - min_val + eps) - 1

                # (0, 1)
                # batch_x_norm = (batch_x - min_val) / (max_val - min_val + eps)

                # batch_x_noisy = add_gaussian_noise_with_snr(batch_x_norm, snr_db=20, seed=i)
                # outputs = self.model(batch_x_noisy)

                outputs = self.model(batch_x_norm)
                f_dim = -1 if self.args.features == 'MS' else 0
                outputs = outputs[:, -self.args.pred_len:, f_dim:]
                target_probs = target_probs[:, -self.args.pred_len:, f_dim:]

                loss = criterion(outputs, target_probs)
                train_loss.append(loss.unsqueeze(0))

                if (i + 1) % 100 == 0:
                    print("\titers: {0}, epoch: {1} | loss: {2:.7f}".format(i + 1, epoch + 1, loss.item()))
                    speed = (time.time() - time_now) / iter_count
                    left_time = speed * ((self.args.train_epochs - epoch) * train_steps - i)
                    print('\tspeed: {:.4f}s/iter; left time: {:.4f}s'.format(speed, left_time))
                    iter_count = 0
                    time_now = time.time()

                loss.backward()
                model_optim.step()

            print("Epoch: {} cost time: {}".format(epoch + 1, time.time() - epoch_time))
            if len(train_loss) > 0:
                train_loss = torch.cat(train_loss).mean().item()
            else:
                train_loss = 0.0
            if not self.args.train_only:
                vali_loss = self.vali(vali_loader, criterion)
                print("Epoch: {0}, Steps: {1} | Train Loss: {2:.7f} Vali Loss: {3:.7f} ".format(
                    epoch + 1, train_steps, train_loss, vali_loss))
                early_stopping(vali_loss, self.model, path)
            else:
                print("Epoch: {0}, Steps: {1} | Train Loss: {2:.7f}".format(
                    epoch + 1, train_steps, train_loss))
                early_stopping(train_loss, self.model, path)

            if early_stopping.early_stop:
                print("Early stopping")
                break

            adjust_learning_rate(model_optim, epoch + 1, self.args)

        best_model_path = path + '/' + 'checkpoint.pth'
        self.model.load_state_dict(torch.load(best_model_path, map_location=self.device))
        return self.model

    def test(self, setting, test=0):
        test_data, test_loader = self._get_data(flag='test')

        if test:
            print('loading model')
            self.model.load_state_dict(torch.load(os.path.join('./checkpoints/' + setting, 'checkpoint.pth')))

        preds = []
        trues = []
        inputx = []
        folder_path = './test_results/' + setting + '/'
        print(f"\n[Debug] The image will be saved to: {os.path.abspath(folder_path)}\n")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        self.model.eval()

        with torch.no_grad():
            for i, (batch_x, batch_y) in enumerate(test_loader):
                batch_x = batch_x.float().to(self.device)
                batch_y = batch_y.float().to(self.device)
                eps = 1e-8
                min_val = batch_x.min(axis=1, keepdims=True).values
                max_val = batch_x.max(axis=1, keepdims=True).values
                batch_x_norm = 2 * (batch_x - min_val) / (max_val - min_val + eps) - 1

                min_val = batch_y.min(axis=1, keepdims=True).values
                max_val = batch_y.max(axis=1, keepdims=True).values
                batch_y_norm = 2 * (batch_y - min_val) / (max_val - min_val + eps) - 1

                hlg_loss = HLGaussLossFromSupport(self.support, sigma=self.sigma).to(self.device)

                probs = hlg_loss.transform_to_probs(batch_y_norm)
                restored = hlg_loss.transform_from_probs(probs)
                mse_restore = torch.mean((restored - batch_y_norm) ** 2).item()
                print(f"batch {i} y → probs → restore MSE: {mse_restore:.6f}")

                outputs = self.model(batch_x_norm)
                f_dim = -1 if self.args.features == 'MS' else 0
                outputs = outputs[:, -self.args.pred_len:, f_dim:]
                pred_continuous = hlg_loss.transform_from_probs(outputs)
                pred_continuous = (pred_continuous+1) * (max_val - min_val + eps)*0.5 + min_val
                # pred_continuous = pred_continuous  * (max_val - min_val + eps) + min_val

                true = batch_y

                preds.append(pred_continuous.detach().cpu().numpy())
                trues.append(batch_y.detach().cpu().numpy())
                inputx.append(batch_x.detach().cpu().numpy())

                if i % 40 == 0:
                    input = batch_x.detach().cpu().numpy()
                    gt = np.concatenate((input[0, :, -1], true[0, :, -1].detach().cpu().numpy()), axis=0)
                    pd = np.concatenate((input[0, :, -1], pred_continuous[0, :, -1].detach().cpu().numpy()), axis=0)
                    output_path = os.path.join(folder_path, f"{i}.png")
                    visual(
                        true=gt,
                        preds=pd,
                        name=output_path,
                        dpi=600,
                        font_size=30
                    )

        preds = np.concatenate(preds, axis=0)
        trues = np.concatenate(trues, axis=0)

        folder_path = './results/' + setting + '/'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        mae, mse, rmse, mape, mspe, rse = metric(preds, trues)
        print('mse:{}, mae:{}'.format(mse, mae))
        f = open("result.txt", 'a')
        f.write(setting + "  \n")
        f.write('mse:{}, mae:{}'.format(mse, mae))
        f.write('\n')
        f.write('\n')
        f.close()

        return
