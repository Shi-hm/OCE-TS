# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from itertools import cycle
#
# # 设置字体为 Times New Roman
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['axes.unicode_minus'] = False
#
# # 全局字体设置
# plt.rcParams.update({
#     'font.size': 20,
#     'axes.labelsize': 20,
#     'xtick.labelsize': 18,
#     'ytick.labelsize': 18,
#     'legend.fontsize': 18,
# })
#
# # 标记和颜色定义
# marker_list = ['D', '^', 's', 'o']
# color_list = ['#FF0000', '#0000FF', '#FF00FF', '#00FF00']
#
# # 1. 读取并清洗数据
# file_path = r"C:\Users\79947\Desktop\有序交叉熵\lookback.xlsx"
# df = pd.read_excel(file_path, sheet_name='Sheet1')
#
# # 关键修复：去除数据集名称中的空格（如 'Weather ' → 'Weather'）
# df['datasets'] = df['datasets'].str.strip()
# df['datasets'] = df['datasets'].fillna(method='ffill')
#
# # 2. 划分数据集（包含 Weather）
# ett_datasets = ['ETTh1', 'ETTh2', 'ETTm1', 'ETTm2', 'Exchange', 'Weather']
# df_ett = df[df['datasets'].isin(ett_datasets)]  # 此时能匹配到 'Weather'
# df_ili = df[df['datasets'] == 'ILI']
#
# # ------------------------ ETT 及 Weather 数据集绘图 ------------------------
# ett_pred_lengths = ['720', '336', '192', '96']
# ett_lookbacks = [48, 96, 192, 336, 504, 720]
#
# # 打印确认是否包含 Weather（调试用）
# print("ETT 类数据集包含：", df_ett['datasets'].unique())
#
# for dataset in df_ett['datasets'].unique():
#     df_ds = df_ett[df_ett['datasets'] == dataset]
#
#     # 初始化误差表格
#     mse_table = pd.DataFrame(index=ett_pred_lengths, columns=ett_lookbacks)
#     mae_table = pd.DataFrame(index=ett_pred_lengths, columns=ett_lookbacks)
#
#     # 填充数据
#     for i, pred_len in enumerate(ett_pred_lengths):
#         window_col = df_ds.columns[1 + i * 3]
#         mse_col = df_ds.columns[2 + i * 3]
#         mae_col = df_ds.columns[3 + i * 3]
#
#         for lb, mse, mae in zip(df_ds[window_col], df_ds[mse_col], df_ds[mae_col]):
#             mse_table.at[pred_len, int(lb)] = mse
#             mae_table.at[pred_len, int(lb)] = mae
#
#     mse_table = mse_table.astype(float)
#     mae_table = mae_table.astype(float)
#
#     # 绘制 MSE 图像
#     fig_mse = plt.figure(figsize=(8, 6))
#     ax_mse = fig_mse.add_subplot(111)
#
#     lines_mse = []
#     labels_mse = []
#     color_cycle = cycle(color_list)
#     marker_cycle = cycle(marker_list)
#     for pred_len in ett_pred_lengths:
#         color = next(color_cycle)
#         marker = next(marker_cycle)
#         line, = ax_mse.plot(ett_lookbacks, mse_table.loc[pred_len],
#                             marker=marker, markersize=10,
#                             label=f'Pred={pred_len}', linewidth=2.5, color=color)
#         lines_mse.append(line)
#         labels_mse.append(f'Pred={pred_len}')
#
#     ax_mse.set_xlabel('Lookback Window Size')
#     ax_mse.set_ylabel('MSE')
#     ax_mse.grid(True, linestyle='--', alpha=0.7)
#     ax_mse.set_xticks(ett_lookbacks)
#
#     fig_mse.legend(lines_mse, labels_mse, loc='lower center',
#                    ncol=len(ett_pred_lengths), bbox_to_anchor=(0.5, -0.1),
#                    frameon=True, fancybox=True, shadow=True)
#     plt.tight_layout(rect=[0, 0.1, 1, 0.95])
#     plt.savefig(f"{dataset}_MSE_results.png", dpi=300, bbox_inches='tight')
#     plt.close()
#
#     # 绘制 MAE 图像
#     fig_mae = plt.figure(figsize=(8, 6))
#     ax_mae = fig_mae.add_subplot(111)
#
#     lines_mae = []
#     labels_mae = []
#     color_cycle = cycle(color_list)
#     marker_cycle = cycle(marker_list)
#     for pred_len in ett_pred_lengths:
#         color = next(color_cycle)
#         marker = next(marker_cycle)
#         line, = ax_mae.plot(ett_lookbacks, mae_table.loc[pred_len],
#                             marker=marker, markersize=10,
#                             label=f'Pred={pred_len}', linewidth=2.5, color=color)
#         lines_mae.append(line)
#         labels_mae.append(f'Pred={pred_len}')
#
#     ax_mae.set_xlabel('Lookback Window Size')
#     ax_mae.set_ylabel('MAE')
#     ax_mae.grid(True, linestyle='--', alpha=0.7)
#     ax_mae.set_xticks(ett_lookbacks)
#
#     fig_mae.legend(lines_mae, labels_mae, loc='lower center',
#                    ncol=len(ett_pred_lengths), bbox_to_anchor=(0.5, -0.1),
#                    frameon=True, fancybox=True, shadow=True)
#     plt.tight_layout(rect=[0, 0.1, 1, 0.95])
#     plt.savefig(f"{dataset}_MAE_results.png", dpi=300, bbox_inches='tight')
#     plt.close()
#
# # ------------------------ ILI 数据集绘图（保持不变） ------------------------
# ili_pred_lengths = ['24', '36', '48', '60']
# ili_lookbacks = [52, 78, 104, 130, 156, 208]
#
# # 定义 ETT 预测长度顺序和 ILI 预测长度的映射关系
# ett_pred_order = ['720', '336', '192', '96']
# ili_mapped_order = ['60', '48', '36', '24']
#
# for dataset in df_ili['datasets'].unique():
#     df_ds = df_ili[df_ili['datasets'] == dataset]
#
#     # 初始化误差表格
#     mse_table = pd.DataFrame(index=ili_pred_lengths, columns=ili_lookbacks)
#     mae_table = pd.DataFrame(index=ili_pred_lengths, columns=ili_lookbacks)
#
#     # 填充数据
#     for i, pred_len in enumerate(ili_pred_lengths):
#         window_col = df_ds.columns[1 + i * 3]
#         mse_col = df_ds.columns[2 + i * 3]
#         mae_col = df_ds.columns[3 + i * 3]
#
#         for lb, mse, mae in zip(df_ds[window_col], df_ds[mse_col], df_ds[mae_col]):
#             mse_table.at[pred_len, int(lb)] = mse
#             mae_table.at[pred_len, int(lb)] = mae
#
#     mse_table = mse_table.astype(float)
#     mae_table = mae_table.astype(float)
#
#     # ------------------------ 绘制 MSE 图像 ------------------------
#     fig_mse = plt.figure(figsize=(8, 6))
#     ax_mse = fig_mse.add_subplot(111)
#
#     lines_mse = []
#     labels_mse = []
#     color_cycle = cycle(color_list)
#     marker_cycle = cycle(marker_list)
#     # 按照映射后的顺序遍历 ILI 预测长度
#     for pred_len in ili_mapped_order:
#         color = next(color_cycle)
#         marker = next(marker_cycle)
#         line, = ax_mse.plot(ili_lookbacks, mse_table.loc[pred_len],
#                             marker=marker, markersize=10,
#                             label=f'Pred={pred_len}', linewidth=2.5, color=color)
#         lines_mse.append(line)
#         labels_mse.append(f'Pred={pred_len}')
#
#     ax_mse.set_xlabel('Lookback Window Size')
#     ax_mse.set_ylabel('MSE')
#     ax_mse.grid(True, linestyle='--', alpha=0.7)
#     ax_mse.set_xticks(ili_lookbacks)
#
#     fig_mse.legend(lines_mse, labels_mse, loc='lower center',
#                    ncol=len(ili_pred_lengths), bbox_to_anchor=(0.5, -0.1),
#                    frameon=True, fancybox=True, shadow=True)
#     plt.tight_layout(rect=[0, 0.1, 1, 0.95])
#     plt.savefig(f"{dataset}_MSE_results.png", dpi=300, bbox_inches='tight')
#     plt.close()
#
#     # ------------------------ 绘制 MAE 图像 ------------------------
#     fig_mae = plt.figure(figsize=(8, 6))
#     ax_mae = fig_mae.add_subplot(111)
#
#     lines_mae = []
#     labels_mae = []
#     color_cycle = cycle(color_list)
#     marker_cycle = cycle(marker_list)
#     # 按照映射后的顺序遍历 ILI 预测长度
#     for pred_len in ili_mapped_order:
#         color = next(color_cycle)
#         marker = next(marker_cycle)
#         line, = ax_mae.plot(ili_lookbacks, mae_table.loc[pred_len],
#                             marker=marker, markersize=10,
#                             label=f'Pred={pred_len}', linewidth=2.5, color=color)
#         lines_mae.append(line)
#         labels_mae.append(f'Pred={pred_len}')
#
#     ax_mae.set_xlabel('Lookback Window Size')
#     ax_mae.set_ylabel('MAE')
#     ax_mae.grid(True, linestyle='--', alpha=0.7)
#     ax_mae.set_xticks(ili_lookbacks)
#
#     fig_mae.legend(lines_mae, labels_mae, loc='lower center',
#                    ncol=len(ili_pred_lengths), bbox_to_anchor=(0.5, -0.1),
#                    frameon=True, fancybox=True, shadow=True)
#     plt.tight_layout(rect=[0, 0.1, 1, 0.95])
#     plt.savefig(f"{dataset}_MAE_results.png", dpi=300, bbox_inches='tight')
#     plt.close()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

# 设置字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams.update({
    'font.size': 30,
    'axes.labelsize': 30,
    'xtick.labelsize': 30,
    'ytick.labelsize': 30,
    'legend.fontsize':30,
    'axes.unicode_minus': False,
})

# 标记与颜色
marker_list = ['D', '^', 's', 'o']
color_list = ['#FF0000', '#0000FF', '#FF00FF', '#00FF00']
ett_pred_lengths = ['720', '336', '192', '96']
ett_lookbacks = [48, 96, 192, 336, 504, 720]
target_datasets = ['ETTh1', 'ETTh2', 'ETTm1', 'ETTm2']

# 读取并清洗数据
file_path = r"C:\Users\79947\Desktop\有序交叉熵\lookback.xlsx"
df = pd.read_excel(file_path, sheet_name='Sheet1')
df['datasets'] = df['datasets'].str.strip()
df['datasets'] = df['datasets'].fillna(method='ffill')
df_ett = df[df['datasets'].isin(target_datasets)]

# 创建子图：2行4列
fig, axes = plt.subplots(2, 4, figsize=(28, 10), sharex=True)

# 保存图例对象
lines_legend = []
labels_legend = []

for idx, dataset in enumerate(target_datasets):
    df_ds = df_ett[df_ett['datasets'] == dataset]

    # 初始化误差表格
    mse_table = pd.DataFrame(index=ett_pred_lengths, columns=ett_lookbacks)
    mae_table = pd.DataFrame(index=ett_pred_lengths, columns=ett_lookbacks)

    # 填充表格
    for i, pred_len in enumerate(ett_pred_lengths):
        window_col = df_ds.columns[1 + i * 3]
        mse_col = df_ds.columns[2 + i * 3]
        mae_col = df_ds.columns[3 + i * 3]

        for lb, mse, mae in zip(df_ds[window_col], df_ds[mse_col], df_ds[mae_col]):
            mse_table.at[pred_len, int(lb)] = mse
            mae_table.at[pred_len, int(lb)] = mae

    mse_table = mse_table.astype(float)
    mae_table = mae_table.astype(float)

    # MSE 子图（第1行）
    ax_mse = axes[0, idx]
    color_cycle = cycle(color_list)
    marker_cycle = cycle(marker_list)

    for pred_len in ett_pred_lengths:
        color = next(color_cycle)
        marker = next(marker_cycle)
        line, = ax_mse.plot(ett_lookbacks, mse_table.loc[pred_len],
                            marker=marker, markersize=8,
                            label = f'Prediction Length = {pred_len}', linewidth=2.5, color=color)
        if idx == 0:
            lines_legend.append(line)
            labels_legend.append(f'Prediction Length = {pred_len}')
    ax_mse.set_title(f'{dataset} - MSE')
    ax_mse.grid(True, linestyle='--', alpha=0.6)
    if idx == 0:
        ax_mse.set_ylabel('MSE')
    ax_mse.set_xticks(ett_lookbacks)

    # MAE 子图（第2行）
    ax_mae = axes[1, idx]
    color_cycle = cycle(color_list)
    marker_cycle = cycle(marker_list)

    for pred_len in ett_pred_lengths:
        color = next(color_cycle)
        marker = next(marker_cycle)
        ax_mae.plot(ett_lookbacks, mae_table.loc[pred_len],
                    marker=marker, markersize=8,
                    linewidth=2.5, color=color)
    ax_mae.set_title(f'{dataset} - MAE')
    ax_mae.grid(True, linestyle='--', alpha=0.6)
    if idx == 0:
        ax_mae.set_ylabel('MAE')
    ax_mae.set_xlabel('Lookback Window Size')
    ax_mae.set_xticks(ett_lookbacks)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])  # bottom 从 0.08 改为 0.12
fig.legend(lines_legend, labels_legend,
           loc='lower center', ncol=4,
           bbox_to_anchor=(0.5, -0.01),  # 向下移出主图区域
           frameon=True, fancybox=True, shadow=True)
plt.savefig("ETT_MSE_MAE_Combined.png", dpi=600, bbox_inches='tight')
plt.show()
