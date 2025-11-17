import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 指定类别数
num_classes = 3

# 生成真实概率分布并四舍五入到最近的十分位
def generate_valid_distribution(num_classes):
    while True:
        distribution = np.random.dirichlet(np.ones(num_classes), 1)[0]
        rounded_distribution = np.round(distribution, 1)
        # 确保所有概率都大于零且总和接近1
        if np.all(rounded_distribution > 0) and np.isclose(np.sum(rounded_distribution), 1):
            return rounded_distribution

# 定义数据
true_dist = generate_valid_distribution(num_classes)
pred_A = generate_valid_distribution(num_classes)
pred_B = generate_valid_distribution(num_classes)
categories = ['Class 1', 'Class 2', 'Class 3']

# 打印生成的概率分布
print("真实概率分布:", true_dist)
print("情况A的预测概率分布:", pred_A)
print("情况B的预测概率分布:", pred_B)

def original_loss(y_true, y_pred):
    epsilon = 1e-8
    return -np.sum(y_true * np.log10(y_pred + epsilon))

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
        return loss

# 计算损失
print("原损失函数 - 情况A:", original_loss(true_dist, pred_A))
print("原损失函数 - 情况B:", original_loss(true_dist, pred_B))

# 实例化损失函数类
criterion = OrderedCrossEntropyLoss()

# 转换为Tensor
true_dist_tensor = torch.tensor(true_dist, dtype=torch.float32)
pred_A_tensor = torch.tensor(pred_A, dtype=torch.float32)
pred_B_tensor = torch.tensor(pred_B, dtype=torch.float32)

# 计算新损失函数
loss_A = criterion(pred_A_tensor, true_dist_tensor)
loss_B = criterion(pred_B_tensor, true_dist_tensor)

print("新损失函数 - 情况A:", loss_A.item())
print("新损失函数 - 情况B:", loss_B.item())

# 绘制对比图
plt.figure(figsize=(15, 6))

# 左图：原始概率分布对比（折线图）
plt.subplot(1, 2, 1)
x = np.arange(len(categories))

# 绘制真实分布
plt.plot(x, true_dist, 'go-', label='True Distribution',
         linewidth=2, markersize=8, markerfacecolor='white', markeredgewidth=2)
# 绘制预测A
plt.plot(x, pred_A, 'bs-', label='Prediction A',
         linewidth=2, markersize=8, markerfacecolor='white', markeredgewidth=2)
# 绘制预测B
plt.plot(x, pred_B, 'r^-', label='Prediction B',
         linewidth=2, markersize=8, markerfacecolor='white', markeredgewidth=2)

# 添加数据点标签
for i, prob in enumerate(true_dist):
    plt.text(x[i], prob+0.02, f'{prob:.1f}', ha='center', fontsize=9)
for i, prob in enumerate(pred_A):
    plt.text(x[i], prob+0.02, f'{prob:.1f}', ha='center', fontsize=9)
for i, prob in enumerate(pred_B):
    plt.text(x[i], prob+0.02, f'{prob:.1f}', ha='center', fontsize=9)

plt.xlabel('Class')
plt.ylabel('Probability')
plt.title('Probability Distribution Comparison (Line Chart)')
plt.xticks(x, categories)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 1.1)

# 右图：累积分布对比
plt.subplot(1, 2, 2)
thresholds = ['P(Y≤1)', 'P(Y≤2)', 'P(Y≤3)']

cum_true = np.cumsum(true_dist)
cum_A = np.cumsum(pred_A)
cum_B = np.cumsum(pred_B)

plt.plot(thresholds, cum_true, 'go-', label='True Distribution', linewidth=2, markersize=8)
plt.plot(thresholds, cum_A, 'bs-', label='Prediction A', linewidth=2, markersize=8)
plt.plot(thresholds, cum_B, 'r^-', label='Prediction B', linewidth=2, markersize=8)

# 添加累积概率标签
for i, cum_prob in enumerate(cum_true):
    plt.text(i, cum_prob+0.02, f'{cum_prob:.1f}', ha='center', fontsize=9)
for i, cum_prob in enumerate(cum_A):
    plt.text(i, cum_prob+0.02, f'{cum_prob:.1f}', ha='center', fontsize=9)
for i, cum_prob in enumerate(cum_B):
    plt.text(i, cum_prob+0.02, f'{cum_prob:.1f}', ha='center', fontsize=9)

plt.xlabel('Cumulative Threshold')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Comparison')
plt.legend()
plt.grid(linestyle='--', alpha=0.7)
plt.ylim(0, 1.1)

# 调整布局并显示
plt.tight_layout()
plt.show()