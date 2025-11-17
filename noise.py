import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 20,
    'axes.titlesize': 20,
    'axes.labelsize': 20,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
})


snr_levels = [-3, 0, 3, 10, 20]
datasets = ['ETTm2', 'Weather']
pred_lens = [96, 192, 336, 720]

mse_data = {
    'ETTm2': {
        96:  [0.117, 0.116, 0.116, 0.118, 0.118],
        192: [0.163, 0.162, 0.162, 0.163, 0.164],
        336: [0.207, 0.206, 0.206, 0.207, 0.209],
        720: [0.275, 0.274, 0.273, 0.277, 0.280]
    },
    'Weather': {
        96:  [0.109, 0.109, 0.108, 0.107, 0.107],
        192: [0.139, 0.138, 0.137, 0.136, 0.136],
        336: [0.173, 0.171, 0.170, 0.168, 0.169],
        720: [0.227, 0.225, 0.224, 0.223, 0.224]
    }
}

mae_data = {
    'ETTm2': {
        96:  [0.229, 0.228, 0.227, 0.229, 0.230],
        192: [0.278, 0.277, 0.276, 0.277, 0.277],
        336: [0.318, 0.317, 0.317, 0.317, 0.318],
        720: [0.373, 0.372, 0.371, 0.372, 0.374]
    },
    'Weather': {
        96:  [0.149, 0.147, 0.145, 0.145, 0.144],
        192: [0.193, 0.191, 0.190, 0.189, 0.189],
        336: [0.232, 0.230, 0.229, 0.228, 0.228],
        720: [0.283, 0.281, 0.280, 0.279, 0.280]
    }
}

markers = ['o', 's', '^', 'D']
colors = ['blue', 'orange']

fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # 取消constrained_layout=True

def plot_metric(ax, data, metric_name):
    for di, dataset in enumerate(datasets):
        for pi, pred in enumerate(pred_lens):
            y_vals = data[dataset][pred]
            x_vals = snr_levels
            sizes = np.array([pred]*len(x_vals)) * 5  # 气泡大小用预测步长调节
            ax.scatter(
                x_vals,
                y_vals,
                s=sizes,
                alpha=0.6,
                color=colors[di],
                edgecolors='k',
                label=f'{dataset}, pred={pred}',
                marker=markers[pi]
            )
    ax.set_xlabel('SNR (dB)', fontsize=12)
    ax.set_ylabel(metric_name, fontsize=12)
    ax.set_title(metric_name, fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='both', labelsize=10)

plot_metric(axs[0], mse_data, 'MSE')
plot_metric(axs[1], mae_data, 'MAE')

from matplotlib.lines import Line2D

legend_elements = []
for di, dataset in enumerate(datasets):
    legend_elements.append(Line2D([0], [0], marker='o', color='w', label=dataset,
                                  markerfacecolor=colors[di], markersize=10))
for pi, pred in enumerate(pred_lens):
    legend_elements.append(Line2D([0], [0], marker=markers[pi], color='k', label=f'prediction length={pred}',
                                  linestyle='None', markersize=10))

fig.legend(
    handles=legend_elements,
    loc='lower center',
    ncol=6,
    fontsize=10,
    bbox_to_anchor=(0.5, 0.03)  # 关键修改：y坐标设为0.1
)

plt.subplots_adjust(bottom=0.2)  # 关键修改：增加底部空间

# 保存为PNG图片（高分辨率）
plt.savefig('snr_performance.png', dpi=600, bbox_inches='tight')
plt.show()