
# import torch.nn as nn
#
# class moving_avg(nn.Module):
#     def __init__(self, kernel_size, stride):
#         super(moving_avg, self).__init__()
#         self.kernel_size = kernel_size
#         self.avg = nn.AvgPool1d(kernel_size=kernel_size, stride=stride, padding=0)
#
#     def forward(self, x):
#         front = x[:, 0:1, :].repeat(1, (self.kernel_size - 1) // 2, 1)
#         end = x[:, -1:, :].repeat(1, (self.kernel_size - 1) // 2, 1)
#         x = torch.cat([front, x, end], dim=1)
#         x = self.avg(x.permute(0, 2, 1))
#         x = x.permute(0, 2, 1)
#         return x
#
#
# class series_decomp(nn.Module):
#     def __init__(self, kernel_size):
#         super(series_decomp, self).__init__()
#         self.moving_avg = moving_avg(kernel_size, stride=1)
#
#     def forward(self, x):
#         moving_mean = self.moving_avg(x)
#         res = x - moving_mean
#         return res, moving_mean
#
# class Model(nn.Module):
#     def __init__(self, configs):
#         super(Model, self).__init__()
#         #输入序列的长度
#         self.seq_len = configs.seq_len
#         #预测序列的长度
#         self.pred_len = configs.pred_len
#
#         # 分解操作中的窗口大小，用于分解时间序列的季节性和趋势性部分
#         kernel_size = 25
#         #将时间序列分解为季节性和趋势性部分
#         self.decompsition = series_decomp(kernel_size)
#         self.individual = configs.individual
#         self.channels = configs.enc_in
#
#         # soft label 支持
#         min_val, max_val, num_bins = 0.0, 1.0, 100
#         support = torch.linspace(min_val, max_val, num_bins)
#         self.prob_transformer = HLGaussLossFromSupport(support, sigma=0.01)
#
#         if self.individual:
#             self.Linear_Seasonal = nn.ModuleList()
#             self.Linear_Trend = nn.ModuleList()
#
#             for i in range(self.channels):
#                 self.Linear_Seasonal.append(nn.Linear(self.seq_len, self.pred_len))
#                 self.Linear_Trend.append(nn.Linear(self.seq_len, self.pred_len))
#
#         else:
#             self.Linear_Seasonal = nn.Linear(self.seq_len, self.pred_len)
#             self.Linear_Trend = nn.Linear(self.seq_len, self.pred_len)
#
#     def forward(self, x):
#         seasonal_init, trend_init = self.decompsition(x)
#         seasonal_init, trend_init = seasonal_init.permute(0, 2, 1), trend_init.permute(0, 2, 1)
#         if self.individual:
#             seasonal_output = torch.zeros([seasonal_init.size(0), seasonal_init.size(1), self.pred_len],
#                                           dtype=seasonal_init.dtype).to(seasonal_init.device)
#             trend_output = torch.zeros([trend_init.size(0), trend_init.size(1), self.pred_len],
#                                        dtype=trend_init.dtype).to(trend_init.device)
#             for i in range(self.channels):
#                 seasonal_output[:, i, :] = self.Linear_Seasonal[i](seasonal_init[:, i, :])
#                 trend_output[:, i, :] = self.Linear_Trend[i](trend_init[:, i, :])
#         else:
#             seasonal_output = self.Linear_Seasonal(seasonal_init)
#             trend_output = self.Linear_Trend(trend_init)
#
#         x = seasonal_output + trend_output
#         x = x.permute(0, 2, 1)
#         return x


import torch
import torch.nn as nn
from layers.Autoformer_EncDec import series_decomp
from loss.hl_gauss import HLGaussLossFromSupport

class Model(nn.Module):
    def __init__(self, configs):
        super(Model, self).__init__()
        self.seq_len = configs.seq_len
        self.pred_len = configs.pred_len
        self.individual = configs.individual
        self.channels = configs.enc_in
        self.sigma = configs.sigma

        kernel_size = 25
        self.decompsition = series_decomp(kernel_size)

        self.num_bins = configs.num_bins
        support = torch.linspace(-1,1, self.num_bins +1 )
        self.prob_transformer = HLGaussLossFromSupport(support, sigma=self.sigma)

        if self.individual:
            self.Linear_Seasonal = nn.ModuleList()
            self.Linear_Trend = nn.ModuleList()
            for i in range(self.channels):
                self.Linear_Seasonal.append(nn.Linear(self.seq_len, self.pred_len * self.num_bins))
                self.Linear_Trend.append(nn.Linear(self.seq_len, self.pred_len * self.num_bins))
        else:
            self.Linear_Seasonal = nn.Linear(self.seq_len, self.pred_len * self.num_bins)
            self.Linear_Trend = nn.Linear(self.seq_len, self.pred_len * self.num_bins)

    def forward(self, x):
        seasonal_init, trend_init = self.decompsition(x)
        seasonal_init, trend_init = seasonal_init.permute(0, 2, 1), trend_init.permute(0, 2, 1)
        B, C, _ = seasonal_init.shape
        if self.individual:
            seasonal_output = torch.zeros([B, C, self.pred_len * self.num_bins], dtype=seasonal_init.dtype).to(x.device)
            trend_output = torch.zeros([B, C, self.pred_len * self.num_bins], dtype=trend_init.dtype).to(x.device)
            for i in range(self.channels):
                seasonal_output[:, i, :] = self.Linear_Seasonal[i](seasonal_init[:, i, :])
                trend_output[:, i, :] = self.Linear_Trend[i](trend_init[:, i, :])
        else:
            seasonal_output = self.Linear_Seasonal(seasonal_init)  # [B, C, pred_len * num_bins]
            trend_output = self.Linear_Trend(trend_init)
        x = seasonal_output + trend_output  # [B, C, pred_len * num_bins]
        x = x.view(B, C, self.pred_len, self.num_bins).permute(0, 2, 1, 3)
        prob = x.softmax(dim=-1)
        return prob























