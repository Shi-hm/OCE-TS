import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams.update({
    'font.size': 30,
    'axes.labelsize': 30,
    'xtick.labelsize': 30,
    'ytick.labelsize': 30,
    'legend.fontsize': 30,
    'axes.unicode_minus': False,
})

# 创建保存图片的目录
output_dir = "analysis_plots"
os.makedirs(output_dir, exist_ok=True)


# 读取 Excel 文件
def load_data():
    # 读取 bin.xlsx 数据
    bin_df = pd.read_excel("C:/Users/79947/Desktop/有序交叉熵/bin.xlsx")

    # 填充空值
    bin_df['datasets'] = bin_df['datasets'].fillna(method='ffill')
    bin_df['bin'] = bin_df['bin'].fillna(method='ffill')

    # 确保数据类型正确
    bin_df['bin'] = bin_df['bin'].astype(int)
    bin_df['pred'] = bin_df['pred'].astype(int)

    # 读取 sigma.xlsx 数据
    sigma_df = pd.read_excel("C:/Users/79947/Desktop/有序交叉熵/sigma.xlsx")

    # 填充空值
    sigma_df['datasets'] = sigma_df['datasets'].fillna(method='ffill')
    sigma_df['sigma'] = sigma_df['sigma'].fillna(method='ffill')

    # 确保数据类型正确
    sigma_df['sigma'] = sigma_df['sigma'].astype(float)
    sigma_df['pred'] = sigma_df['pred'].astype(int)

    return bin_df, sigma_df


# 绘制所有MSE图表在一张图上（适合双栏）
def plot_combined_mse(bin_df, sigma_df, save=False):
    # 获取所有数据集
    datasets = sorted(list(set(bin_df['datasets'].unique()) & set(sigma_df['datasets'].unique())))

    # 不足4个数据集时用空值填充
    while len(datasets) < 4:
        datasets.append(None)

    # 颜色配置（仅修改图例标签文本）
    pred_styles = {
        96: {'marker': 'o', 'color': '#E60000', 'label': 'Prediction length=96'},  # 改为完整的"Prediction"
        192: {'marker': 's', 'color': '#0066FF', 'label': 'Prediction length=192'},
        336: {'marker': '^', 'color': '#FF9900', 'label': 'Prediction length=336'},
        720: {'marker': 'D', 'color': '#9900FF', 'label': 'Prediction length=720'}
    }

    # 创建2行4列的图表
    fig, axes = plt.subplots(2, 4, figsize=(28, 10))
    fig.subplots_adjust(bottom=0.2, wspace=0.3, hspace=0.5)

    # 第一行：绘制bin对MSE的影响
    for i, dataset in enumerate(datasets[:4]):
        ax = axes[0, i]

        if dataset is None:
            ax.axis('off')
            continue

        dataset_df = bin_df[bin_df['datasets'] == dataset]
        bin_values = sorted(dataset_df['bin'].unique())

        for pred, style in pred_styles.items():
            pred_df = dataset_df[dataset_df['pred'] == pred]
            if not pred_df.empty:
                ax.plot(pred_df['bin'], pred_df['MSE'],
                        marker=style['marker'],
                        color=style['color'],
                        linestyle='-',
                        linewidth=2,
                        markersize=7,
                        label=style['label'] if i == 0 else "")  # 图例标签已更新

        ax.set_xlabel('Bin size', labelpad=8)
        ax.set_ylabel('MSE', labelpad=8)
        ax.set_title(f'{dataset}', pad=10)
        ax.set_xticks(bin_values)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.tick_params(axis='both', which='major', labelsize=14)

    # 第二行：绘制sigma对MSE的影响
    for i, dataset in enumerate(datasets[:4]):
        ax = axes[1, i]

        if dataset is None:
            ax.axis('off')
            continue

        dataset_df = sigma_df[sigma_df['datasets'] == dataset]
        sigma_values = sorted(dataset_df['sigma'].unique())

        for pred, style in pred_styles.items():
            pred_df = dataset_df[dataset_df['pred'] == pred]
            if not pred_df.empty:
                ax.semilogx(pred_df['sigma'], pred_df['MSE'],
                            marker=style['marker'],
                            color=style['color'],
                            linestyle='-',
                            linewidth=2,
                            markersize=7,
                            label=style['label'] if i == 0 else "")  # 图例标签已更新

        ax.set_xlabel('Sigma (σ) - log scale', labelpad=8)
        ax.set_ylabel('MSE', labelpad=8)
        ax.set_title(f'{dataset}', pad=10)
        ax.set_xticks(sigma_values)
        ax.set_xticklabels([f"{s:.3f}" for s in sigma_values], fontsize=12)
        ax.grid(True, which='both', linestyle='--', alpha=0.6)
        ax.tick_params(axis='both', which='major', labelsize=14)

    # 添加统一图例（标签已自动更新为修改后的值）
    handles, labels = axes[0, 0].get_legend_handles_labels()
    plt.tight_layout(rect=[0, 0.02, 1, 0.95])
    fig.legend(handles, labels,
               loc='lower center', ncol=4,
               bbox_to_anchor=(0.5, -0.025),
               frameon=True, fancybox=True, columnspacing=2.0)

    if save:
        plt.savefig(f'{output_dir}/combined_MSE_plots_double_column.png',
                    dpi=600, bbox_inches='tight')
        plt.close()
    else:
        plt.show()


# 主程序
if __name__ == "__main__":
    bin_data, sigma_data = load_data()
    plot_combined_mse(bin_data, sigma_data, save=True)
    print(f"Combined MSE plot saved to: {output_dir} directory")