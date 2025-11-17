# import numpy as np
# import matplotlib.pyplot as plt
# import random
#
#
# # Function to check if a point satisfies Region 1 constraints
# def in_region1(p_A, p_B):
#     if not (np.isclose(np.sum(p_A), 1) and np.isclose(np.sum(p_B), 1)):
#         return False
#     if not (np.all(p_A >= 0) and np.all(p_B >= 0)):
#         return False
#     if not (p_A[1] > p_A[0] and p_A[1] > p_A[2]):
#         return False
#     if not (p_B[2] > p_B[0] and p_B[2] > p_B[1]):
#         return False
#     return True
#
#
# # Function to check if a point satisfies Region 2 constraints
# def in_region2(p_A, p_B):
#     if not in_region1(p_A, p_B):
#         return False
#     if not (p_A[0] < p_B[0]):
#         return False
#     try:
#         log_val_A = np.log(p_A[0]) + np.log(p_A[0] + p_A[1])
#         log_val_B = np.log(p_B[0]) + np.log(p_B[0] + p_B[1])
#         if not (log_val_A > log_val_B):
#             return False
#     except ValueError:
#         return False
#     if not (0 < p_A[0] < 0.5):
#         return False
#     if not (p_A[0] < p_B[0] < 0.5):
#         return False
#     return True
#
#
# # Generate sample points satisfying Region 1 constraints
# def generate_region1_samples(n=10000):
#     samples = []
#     while len(samples) < n:
#         p_A = np.random.dirichlet([1, 1, 1])
#         if not (p_A[1] > p_A[0] and p_A[1] > p_A[2]):
#             continue
#         p_B = np.random.dirichlet([1, 1, 1])
#         if not (p_B[2] > p_B[0] and p_B[2] > p_B[1]):
#             continue
#         if in_region1(p_A, p_B):
#             samples.append((p_A, p_B))
#     return samples
#
#
# # Generate sample points satisfying Region 2 constraints
# def generate_region2_samples(n=10000):
#     samples = []
#     while len(samples) < n:
#         p1_A = random.uniform(0.01, 0.49)
#         p1_B = random.uniform(p1_A + 0.01, 0.49)
#         p2_A = random.uniform(max(p1_A, 0.34), 0.99 - p1_A)
#         p3_A = 1 - p1_A - p2_A
#         p3_B = random.uniform(max(p1_B, 0.34), 0.99 - p1_B)
#         p2_B = 1 - p1_B - p3_B
#         p_A = np.array([p1_A, p2_A, p3_A])
#         p_B = np.array([p1_B, p2_B, p3_B])
#         try:
#             log_val_A = np.log(p_A[0]) + np.log(p_A[0] + p_A[1])
#             log_val_B = np.log(p_B[0]) + np.log(p_B[0] + p_B[1])
#             if log_val_A <= log_val_B:
#                 continue
#         except ValueError:
#             continue
#         if in_region2(p_A, p_B):
#             samples.append((p_A, p_B))
#     return samples
#
#
# # Create radar chart with adjustable font sizes
# def plot_radar_chart(region1_samples, region2_samples):
#     # Define angles and labels
#     angles = np.linspace(0, 2 * np.pi, 6, endpoint=False).tolist()
#     labels = ['p₁ᴬ', 'p₂ᴬ', 'p₃ᴬ', 'p₁ᴮ', 'p₂ᴮ', 'p₃ᴮ']
#
#     # Calculate boundaries
#     region1_min = np.array([min(s[0][0] for s in region1_samples),
#                             min(s[0][1] for s in region1_samples),
#                             min(s[0][2] for s in region1_samples),
#                             min(s[1][0] for s in region1_samples),
#                             min(s[1][1] for s in region1_samples),
#                             min(s[1][2] for s in region1_samples)])
#
#     region1_max = np.array([max(s[0][0] for s in region1_samples),
#                             max(s[0][1] for s in region1_samples),
#                             max(s[0][2] for s in region1_samples),
#                             max(s[1][0] for s in region1_samples),
#                             max(s[1][1] for s in region1_samples),
#                             max(s[1][2] for s in region1_samples)])
#
#     region2_min = np.array([min(s[0][0] for s in region2_samples),
#                             min(s[0][1] for s in region2_samples),
#                             min(s[0][2] for s in region2_samples),
#                             min(s[1][0] for s in region2_samples),
#                             min(s[1][1] for s in region2_samples),
#                             min(s[1][2] for s in region2_samples)])
#
#     region2_max = np.array([max(s[0][0] for s in region2_samples),
#                             max(s[0][1] for s in region2_samples),
#                             max(s[0][2] for s in region2_samples),
#                             max(s[1][0] for s in region2_samples),
#                             max(s[1][1] for s in region2_samples),
#                             max(s[1][2] for s in region2_samples)])
#
#
#     # Create figure
#     fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))
#
#     # Close angles and labels
#     angles += angles[:1]
#     labels += labels[:1]
#
#     # Plot boundaries
#     max_values1 = np.append(region1_max, region1_max[0])
#     ax.plot(angles, max_values1, 'r-', linewidth=2, label='Region 1 ')
#
#     max_values2 = np.append(region2_max, region2_max[0])
#     ax.plot(angles, max_values2, 'b-', linewidth=2, label='Region 2 ')
#
#
#     # Fill regions
#     ax.fill(angles, max_values1, 'r', alpha=0.1)
#     ax.fill(angles, max_values2, 'b', alpha=0.3)
#
#     # Plot sample points
#     for i, ((p_A, p_B), color) in enumerate(zip(random.sample(region1_samples, 5), ['red'] * 5)):
#         values = np.append([p_A[0], p_A[1], p_A[2], p_B[0], p_B[1], p_B[2]], p_A[0])
#         ax.plot(angles, values, color=color, linestyle='--', alpha=0.3)
#
#     for i, ((p_A, p_B), color) in enumerate(zip(random.sample(region2_samples, 5), ['blue'] * 5)):
#         values = np.append([p_A[0], p_A[1], p_A[2], p_B[0], p_B[1], p_B[2]], p_A[0])
#         ax.plot(angles, values, color=color, linestyle='--', alpha=0.3)
#
#     # ========== 字体大小调整部分 ==========
#     # 设置坐标轴标签字体大小
#     ax.set_xticks(angles[:-1])
#     ax.set_xticklabels(labels[:-1], fontsize=25)  # 维度标签（如p₁ᴬ）
#
#     # 设置y轴刻度字体大小
#     ax.tick_params(axis='y', labelsize=30)  # 径向刻度（0-1的数值）
#
#     # 设置网格线相关字体（如果需要）
#     ax.grid(True)
#
#     # # 设置图例字体大小
#     # ax.legend(loc='upper right', fontsize=20)  # 图例（Region 1/2）
#     ax.legend(
#         loc='upper left',  # 定位点
#         bbox_to_anchor=(0.75, 0.93),  # 相对坐标 (1.05,1) 表示图表外右上
#         borderaxespad=0.,  # 与坐标轴的间距
#         fontsize=28
#     )
#
#     # 设置标题字体大小
#     plt.title('Probability Range Radar', fontsize=35,loc='center' )  # 图表标题
#
#     plt.tight_layout()
#     return fig
#
#
# # Main function
# def main():
#     region1_samples = generate_region1_samples(1000)
#     region2_samples = generate_region2_samples(1000)
#     fig = plot_radar_chart(region1_samples, region2_samples)
#     plt.show()
#
#
# if __name__ == "__main__":
#     main()


import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt


plt.rcParams.update({
    'font.size': 20,              # 全局字体大小
    'axes.titlesize': 18,         # 标题字体大小
    'axes.labelsize': 14,         # 坐标轴标签字体大小
    'xtick.labelsize': 14,        # X轴刻度字体大小
    'ytick.labelsize': 20,        # Y轴刻度字体大小
    'legend.fontsize': 15,        # 图例字体大小
    'figure.titlesize': 16        # 图表总标题字体大小
})

# ========= 损失函数 =========
def original_loss(y_true, y_pred):
    epsilon = 1e-8
    return -np.sum(y_true * np.log10(y_pred + epsilon))

class OrderedCrossEntropyLoss(nn.Module):
    def __init__(self, epsilon=1e-8):
        super().__init__()
        self.epsilon = epsilon

    def forward(self, pred_probs, true_probs):
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

# ========= 输入分布 =========
true_dist = np.array([0.8, 0.1, 0.1])
pred_A = np.array([0.3, 0.5, 0.2])
pred_B = np.array([0.4, 0.1, 0.5])

# ========= 损失计算 =========
ce_A = original_loss(true_dist, pred_A)
ce_B = original_loss(true_dist, pred_B)

criterion = OrderedCrossEntropyLoss()
true_tensor = torch.tensor(true_dist, dtype=torch.float32)
pred_A_tensor = torch.tensor(pred_A, dtype=torch.float32)
pred_B_tensor = torch.tensor(pred_B, dtype=torch.float32)

ord_A = criterion(pred_A_tensor, true_tensor).item()
ord_B = criterion(pred_B_tensor, true_tensor).item()

# ========= 计算重叠面积（交集面积） =========
def overlap_area(p, q):
    return np.sum(np.minimum(p, q))

overlap_A = overlap_area(true_dist, pred_A)
overlap_B = overlap_area(true_dist, pred_B)

# ========= 输出结果 =========
print("真实概率分布:", true_dist)
print("情况A的预测概率分布:", pred_A)
print("情况B的预测概率分布:", pred_B)
print("原损失函数 - 情况A:", ce_A)
print("原损失函数 - 情况B:", ce_B)
print("新损失函数 - 情况A:", ord_A)
print("新损失函数 - 情况B:", ord_B)
print("重叠面积 - 情况A:", overlap_A)
print("重叠面积 - 情况B:", overlap_B)

# ========= 雷达图绘制 =========
def plot_radar(true_dist, pred_A, pred_B):
    labels = ['Class 0', 'Class 1', 'Class 2']
    num_vars = len(labels)
    # 计算角度（闭合雷达图需要多一个角度回到起点）
    angles = np.linspace(0, 2 * np.pi, num_vars + 1)

    # 辅助函数：闭合数据（首尾相连）
    def prepare(data):
        return np.concatenate([data, [data[0]]])  # 闭合雷达图

    # 处理数据
    true_r = prepare(true_dist)
    A_r = prepare(pred_A)
    B_r = prepare(pred_B)

    # 绘制雷达图
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 绘制三条曲线
    ax.plot(angles, true_r, 'g-', label='True', linewidth=2)
    ax.fill(angles, true_r, 'g', alpha=0.2)  # 填充区域

    ax.plot(angles, A_r, 'b-', label='Pred A', linewidth=2)
    ax.fill(angles, A_r, 'b', alpha=0.2)

    ax.plot(angles, B_r, 'r-', label='Pred B', linewidth=2)
    ax.fill(angles, B_r, 'r', alpha=0.2)

    # 设置坐标轴刻度（固定为0.2、0.4、0.6、0.8）
    ax.set_rticks([0.2, 0.4, 0.6,0.8])  # 径向刻度
    ax.set_ylim(0, 0.8)  # 限制范围为0到1（概率分布常用范围）

    # 设置角度标签
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)  # 去掉最后一个重复角度


    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.05))

    plt.tight_layout()
    plt.savefig("Probability Distribution Comparison", dpi=300, bbox_inches='tight')
    plt.show()

plot_radar(true_dist, pred_A, pred_B)



