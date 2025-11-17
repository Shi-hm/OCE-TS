import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import seaborn as sns


class ModelComparisonPlot:
    def __init__(self, figsize=(12, 8)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.models = []

    def add_model(self, name, x_value, y_value, size_value, color,
                  annotation_offset=(0, 0), memory_info=None):
        """
        添加模型到图表

        Parameters:
        - name: 模型名称
        - x_value: X轴值（如训练时间）
        - y_value: Y轴值（如MSE）
        - size_value: 圆圈大小值（如参数量）
        - color: 颜色
        - annotation_offset: 标注偏移量
        - memory_info: 内存信息字符串
        """
        self.models.append({
            'name': name,
            'x': x_value,
            'y': y_value,
            'size': size_value,
            'color': color,
            'offset': annotation_offset,
            'memory': memory_info
        })

    def plot(self, title, xlabel, ylabel, xlim=None, ylim=None,
             add_memory_box=False, memory_box_info=None):
        """
        绘制图表
        """
        # 绘制散点
        for model in self.models:
            self.ax.scatter(model['x'], model['y'], s=model['size'],
                            c=model['color'], alpha=0.7,
                            edgecolors='white', linewidth=2)

            # 添加标注
            offset_x, offset_y = model['offset']
            self.ax.annotate(model['name'],
                             (model['x'], model['y']),
                             xytext=(model['x'] + offset_x, model['y'] + offset_y),
                             fontsize=10, fontweight='bold', ha='center')

        # 添加内存信息框
        if add_memory_box and memory_box_info:
            self._add_memory_box(memory_box_info)

        # 设置标签和标题
        self.ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
        self.ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
        self.ax.set_title(title, fontsize=16, fontweight='bold')

        # 设置范围
        if xlim:
            self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)

        # 美化
        self.ax.grid(True, alpha=0.3)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        plt.tight_layout()
        return self.fig, self.ax

    def _add_memory_box(self, info):
        """添加内存信息框"""
        x, y, width, height = info['position']
        box = Rectangle((x, y), width, height, linewidth=1,
                        edgecolor='gray', facecolor='white',
                        linestyle='--', alpha=0.8)
        self.ax.add_patch(box)

        # 添加文本
        for i, text in enumerate(info['texts']):
            self.ax.text(x + 2, y + height - 0.01 - i * 0.01, text,
                         fontsize=8, color='gray')


# 使用示例
plot = ModelComparisonPlot()

# 添加模型数据
plot.add_model('PatchTST', 35, 0.16, 800, 'orange', (0, -0.02))
plot.add_model('iTransformer', 25, 0.18, 600, 'blue', (-8, 0.01))
plot.add_model('Transformer', 85, 0.34, 1200, 'green', (5, 0.01))

# 绘制图表
memory_info = {
    'position': (25, 0.32, 30, 0.08),
    'texts': ['Memory Footprint', '0.85GB 0.95GB 1.10GB']
}

fig, ax = plot.plot(
    title='Weather [21 Variables]',
    xlabel='Training Time (ms/iter)',
    ylabel='MSE',
    xlim=(20, 120),
    ylim=(0.12, 0.40),
    add_memory_box=True,
    memory_box_info=memory_info
)

plt.show()
# 保存为高分辨率图像
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('model_comparison.pdf', bbox_inches='tight')  # 矢量图