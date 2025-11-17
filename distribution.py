import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体和样式（针对双栏文件放大字体）
plt.rcParams.update({
    'font.family': 'Times New Roman',
    'axes.unicode_minus': False,
    'font.size': 30,  # 基础字体放大
    'axes.labelsize': 30,
    'xtick.labelsize': 30,
    'ytick.labelsize': 30,
    'legend.fontsize': 30,
    'axes.titlesize': 30,
})

# 数据准备（保持不变）
data = []
distributions = ['truncated Gaussian', 'T', 'Laplacian']
perd_lens = [96, 192, 336, 720]
datasets = ['ETTh1', 'ETTh2', 'ETTm1', 'ETTm2']

values = [
    # truncated Gaussian
    [0.341, 0.395, 0.197, 0.313, 0.195, 0.308, 0.118, 0.230],  # 96
    [0.416, 0.445, 0.248, 0.352, 0.279, 0.363, 0.167, 0.279],  # 192
    [0.491, 0.491, 0.313, 0.395, 0.372, 0.407, 0.211, 0.319],  # 336
    [0.547, 0.528, 0.379, 0.435, 0.479, 0.466, 0.277, 0.367],  # 720

    # T
    [0.357, 0.403, 0.196, 0.312, 0.196, 0.305, 0.118, 0.230],  # 96
    [0.429, 0.450, 0.248, 0.352, 0.280, 0.360, 0.164, 0.277],  # 192
    [0.504, 0.495, 0.313, 0.395, 0.362, 0.404, 0.209, 0.318],  # 336
    [0.557, 0.528, 0.379, 0.435, 0.465, 0.460, 0.282, 0.374],  # 720

    # Laplacian
    [0.355, 0.403, 0.197, 0.313, 0.198, 0.306, 0.119, 0.230],  # 96
    [0.427, 0.449, 0.248, 0.352, 0.294, 0.366, 0.168, 0.280],  # 192
    [0.505, 0.496, 0.313, 0.395, 0.373, 0.408, 0.211, 0.319],  # 336
    [0.557, 0.528, 0.379, 0.435, 0.479, 0.466, 0.297, 0.384]  # 720
]

# 构建数据框（保持不变）
index = 0
for dist in distributions:
    for perd in perd_lens:
        vals = values[index]
        for i, dataset in enumerate(datasets):
            data.append({
                'distribution': dist,
                'perd_len': perd,
                'dataset': dataset,
                'MSE': vals[2 * i],
                'MAE': vals[2 * i + 1]
            })
        index += 1

df = pd.DataFrame(data)

# 合并为一张图：上MSE，下MAE，共享底部图例
fig, axes = plt.subplots(2, 4, figsize=(28, 10), sharex=True, sharey='row')  # 适应双栏的尺寸


# 为 MSE 和 MAE 分别定义颜色
mse_colors = ['#FF0000', '#0000FF', '#FF00FF']  # MSE 三种分布颜色
mae_colors = ['#00FF00', '#FFA500', '#808080']  # MAE 三种分布颜色

# 绘制 MSE（第一行子图）和 MAE（第二行子图）
for row, metric in enumerate(['MSE', 'MAE']):
    # 计算当前指标的全局最大值，统一行内 y 轴范围
    global_max = df[metric].max() * 1.15  # 留更多余量避免标签溢出

    for col, dataset in enumerate(datasets):
        ax = axes[row, col]
        dataset_data = df[df['dataset'] == dataset]
        pivot_data = dataset_data.pivot(index='perd_len', columns='distribution', values=metric)

        # 条形图参数
        bar_width = 0.25
        x = np.arange(len(pivot_data))  # 预测长度位置

        # 根据指标选取对应颜色列表
        color_list = mse_colors if metric == 'MSE' else mae_colors

        # 绘制分组条形图
        for j, dist in enumerate(distributions):
            x_pos = x + (j - 1) * bar_width  # 居中对齐
            bars = ax.bar(
                x_pos,
                pivot_data[dist],
                width=bar_width,
                color=color_list[j],
                edgecolor='black',
                linewidth=2,  # 加粗边框
                label=dist if (row == 0 and col == 0) else ""  # 仅第一个子图添加标签（后续统一整理图例）
            )

        # 子图设置
        ax.set_title(dataset, fontsize=24, pad=15)  # 增加标题间距
        ax.set_xlabel('Prediction Length', fontsize=24, labelpad=10)
        ax.set_xticks(x)
        ax.set_xticklabels(pivot_data.index, fontsize=22)
        ax.grid(True, linestyle='--', alpha=0.7, linewidth=1.5)
        ax.set_ylim(0, global_max)

        # 仅每行第一列显示 y 轴标签
        if col == 0:
            ax.set_ylabel(metric, fontsize=24, labelpad=10)

        # 放大刻度线
        ax.tick_params(axis='both', length=8, width=2)

# 整理图例：分别获取 MSE、MAE 对应的分布标签及颜色
mse_handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in mse_colors]
mae_handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in mae_colors]
all_handles = mse_handles + mae_handles
all_labels = [f'{metric}_' + dist for metric, color_list in zip(['MSE', 'MAE'], [mse_colors, mae_colors]) for dist in distributions]

# 底部添加共享图例（放大尺寸），区分 MSE、MAE 颜色
fig.legend(
    all_handles, all_labels,
    fontsize=30,
    loc='lower center',
    ncol=3,  # 横向排列
    bbox_to_anchor=(0.5, -0.09),  # 贴近底部，微调避免重叠
    frameon=True,
    fancybox=True,
    shadow=True,
    handlelength=3,  # 加长图例标记
    handletextpad=1.5,  # 标记与文字间距
    columnspacing=5,  # 列间距
    borderaxespad=2  # 边框间距
)

# 调整布局（为双栏优化）
plt.tight_layout(rect=[0, 0.08, 1, 0.95])  # 预留图例和标题空间
plt.subplots_adjust(hspace=0.35, wspace=0.15)  # 调整子图间距

# 保存为高分辨率图片（适合印刷）
plt.savefig('MSE_MAE_combined_diff_colors.png', dpi=600, bbox_inches='tight')
plt.close()