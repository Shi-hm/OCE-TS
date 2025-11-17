import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# 设置全局字体为 Times New Roman，统一字号
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20  # 全局字体大小
plt.rcParams['axes.titlesize'] = 20  # 子图标题大小
plt.rcParams['axes.labelsize'] = 20  # 坐标轴标签大小
plt.rcParams['legend.fontsize'] = 20  # 图例字体大小
plt.rcParams['xtick.labelsize'] = 20  # x 轴刻度字体
plt.rcParams['ytick.labelsize'] = 20  # y 轴刻度字体

# 原始数据
raw_data = [
    ['ETTh1', 96, 0.341, 0.645, 0.395, 0.523],
    ['ETTh1', 192, 0.416, 0.766, 0.445, 0.576],
    ['ETTh1', 336, 0.491, 0.910, 0.491, 0.633],
    ['ETTh1', 720, 0.547, 1.021, 0.528, 0.697],
    ['ETTh2', 96, 0.197, 0.314, 0.313, 0.388],
    ['ETTh2', 192, 0.248, 0.411, 0.352, 0.450],
    ['ETTh2', 336, 0.313, 0.540, 0.395, 0.518],
    ['ETTh2', 720, 0.379, 0.729, 0.435, 0.609],
    ['ETTm1', 96, 0.195, 0.357, 0.308, 0.391],
    ['ETTm1', 192, 0.279, 0.542, 0.363, 0.479],
    ['ETTm1', 336, 0.372, 0.685, 0.407, 0.543],
    ['ETTm1', 720, 0.479, 0.886, 0.466, 0.627],
    ['ETTm2', 96, 0.118, 0.188, 0.230, 0.284],
    ['ETTm2', 192, 0.167, 0.275, 0.279, 0.355],
    ['ETTm2', 336, 0.211, 0.373, 0.319, 0.421],
    ['ETTm2', 720, 0.286, 0.581, 0.377, 0.536],
    ['Exchange', 96, 0.055, 0.088, 0.148, 0.184],
    ['Exchange', 192, 0.107, 0.216, 0.224, 0.310],
    ['Exchange', 336, 0.199, 0.403, 0.322, 0.448],
    ['Exchange', 720, 0.521, 1.125, 0.578, 0.844],
    ['ILI', 24, 0.570, 0.801, 0.458, 0.557],
    ['ILI', 36, 0.749, 1.504, 0.558, 0.815],
    ['ILI', 48, 1.180, 2.874, 0.710, 1.145],
    ['ILI', 60, 1.282, 3.259, 0.738, 1.215],
    ['Weather', 96, 0.107, 0.234, 0.144, 0.208],
    ['Weather', 192, 0.140, 0.438, 0.190, 0.335],
    ['Weather', 336, 0.169, 0.645, 0.228, 0.437],
    ['Weather', 720, 0.225, 0.878, 0.283, 0.558],
]

df = pd.DataFrame(raw_data, columns=['dataset', 'pred_len', 'MSE_ours', 'MSE_CE', 'MAE_ours', 'MAE_CE'])

# 创建输出目录
output_dir_mse = "plots_MSE"
output_dir_mae = "plots_MAE"
os.makedirs(output_dir_mse, exist_ok=True)
os.makedirs(output_dir_mae, exist_ok=True)

# 调整柱子宽度和颜色
bar_width = 0.45
color_ours = '#1f77b4'  # 深蓝色（替代skyblue，饱和度更高）
color_ce = '#ff7f0e'    # 橙红色（替代orange，更鲜艳）

# 生成MSE图像
for dataset, group in df.groupby('dataset'):
    group = group.sort_values('pred_len')
    pred_lens = group['pred_len'].astype(str).tolist()
    x = np.arange(len(pred_lens))

    plt.figure(figsize=(10, 6))
    plt.bar(x - bar_width / 2, group['MSE_ours'], width=bar_width, label='OCE', color=color_ours)
    plt.bar(x + bar_width / 2, group['MSE_CE'], width=bar_width, label='CE', color=color_ce)

    plt.xlabel('Prediction Length', fontsize=20)
    plt.ylabel('MSE', fontsize=20)
    plt.xticks(x, pred_lens)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    plt.savefig(os.path.join(output_dir_mse, f"{dataset}_MSE.png"))
    plt.close()

# 生成MAE图像
for dataset, group in df.groupby('dataset'):
    group = group.sort_values('pred_len')
    pred_lens = group['pred_len'].astype(str).tolist()
    x = np.arange(len(pred_lens))

    plt.figure(figsize=(10, 6))
    plt.bar(x - bar_width / 2, group['MAE_ours'], width=bar_width, label='OCE', color=color_ours)
    plt.bar(x + bar_width / 2, group['MAE_CE'], width=bar_width, label='CE', color=color_ce)

    plt.xlabel('Prediction Length', fontsize=20)
    plt.ylabel('MAE', fontsize=20)
    plt.xticks(x, pred_lens)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    plt.savefig(os.path.join(output_dir_mae, f"{dataset}_MAE.png"))
    plt.close()

print(f"✅ MSE图像已保存至：{output_dir_mse}/")
print(f"✅ MAE图像已保存至：{output_dir_mae}/")