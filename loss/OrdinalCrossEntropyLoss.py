import torch
import torch.nn as nn


class OrderedCrossEntropyLoss(nn.Module):
    def __init__(self, epsilon=1e-8):
        super().__init__()
        self.epsilon = epsilon

    def forward(self, pred_probs, true_probs):
        if pred_probs.shape != true_probs.shape:
            raise ValueError(f"Shape mismatch: pred_probs: {pred_probs.shape}, true_probs: {true_probs.shape}")

        pred_cumulative = torch.cumsum(pred_probs, dim=-1)
        true_cumulative = torch.cumsum(true_probs, dim=-1)

        pred_cumulative = torch.clamp(pred_cumulative, min=self.epsilon, max=1 - self.epsilon)
        true_cumulative = torch.clamp(true_cumulative, min=self.epsilon, max=1 - self.epsilon)

        loss = 0.0
        for c in range(pred_probs.shape[-1] - 1):
            p_true_le = true_cumulative[..., c]
            p_true_gt = 1 - p_true_le
            p_pred_le = pred_cumulative[..., c]
            loss_c = (p_true_le * torch.log(p_pred_le + self.epsilon) +
                      p_true_gt * torch.log(1 - p_pred_le + self.epsilon))
            loss -= loss_c.mean()
        # criterion = nn.CrossEntropyLoss()
        # loss = criterion(pred_probs, true_probs)
        return loss


