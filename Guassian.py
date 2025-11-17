import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# 设置中文字体支持
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def plot_truncated_gaussian(li, wi, mu, sigma, ax, color, label):
    """
    绘制区间 [li, li+wi] 上的截断高斯分布

    参数:
    li: 区间左端点
    wi: 区间宽度
    mu: 均值 (必须在区间内)
    sigma: 标准差
    ax: matplotlib 轴对象
    color: 线条颜色
    label: 图例标签
    """
    # 计算截断高斯分布的 a 和 b（标准化区间）
    a, b = (li - mu) / sigma, (li + wi - mu) / sigma

    # 生成 x 值（区间内更密集）
    x = np.linspace(li - 0.5 * wi, li + wi + 0.5 * wi, 1000)

    # 计算截断高斯分布的概率密度函数值
    pdf = truncnorm.pdf(x, a, b, loc=mu, scale=sigma)

    # 绘制分布曲线
    ax.plot(x, pdf, color=color, linewidth=2, label=label)

    # 标记均值位置（虚线仅到分布曲线顶部）
    pdf_at_mu = truncnorm.pdf(mu, a, b, loc=mu, scale=sigma)
    ax.plot([mu, mu], [0, pdf_at_mu], color=color, linestyle='--', alpha=0.7)

    # 标记区间边界
    ax.axvline(x=li, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=li + wi, color='gray', linestyle=':', alpha=0.5)


def main():
    # 设置固定的标准差
    sigma = 0.2

    # 定义三个不同的区间和对应的均值
    distributions = [
        {"li": 0, "wi": 1, "mu": 0.2, "color": "blue", "label": "分布1 (μ=0.2)"},
        {"li": 0, "wi": 1, "mu": 0.5, "color": "green", "label": "分布2 (μ=0.5)"},
        {"li": 0, "wi": 1, "mu": 0.8, "color": "red", "label": "分布3 (μ=0.8)"}
    ]

    # 创建图形
    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    # 绘制每个分布
    for dist in distributions:
        plot_truncated_gaussian(
            li=dist["li"],
            wi=dist["wi"],
            mu=dist["mu"],
            sigma=sigma,
            ax=ax,
            color=dist["color"],
            label=dist["label"]
        )

    # 设置图表属性
    plt.title('区间 [0,1] 上的截断高斯分布 (σ=0.2)')
    plt.xlabel('x')
    plt.ylabel('概率密度')
    plt.xlim(-0.2, 1.2)


    # 显示图形
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()