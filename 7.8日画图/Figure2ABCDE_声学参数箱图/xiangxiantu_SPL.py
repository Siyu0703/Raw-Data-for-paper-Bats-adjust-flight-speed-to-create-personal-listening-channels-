# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:53:00 2024

@author: cattree
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
from scipy.interpolate import CubicSpline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import matplotlib as mpl
from matplotlib import rcParams
import matplotlib.font_manager as font_manager

# 路径替换为你Helvetica.ttf字体文件的实际路径
font_path = 'D:/app/helvetica/HelveticaTTF/Helvetica/Helvetica.ttf'

# 添加这个字体路径
font_manager.fontManager.addfont(font_path)
# 设置全局字体
rcParams['font.family'] = 'Helvetica'
# 如果matplotlib没有识别到Helvetica，可以使用下面的方式设置
# rcParams['font.sans-serif'] = 'Helvetica'
# 设置全局字体为Helvetica
matplotlib.rcParams['font.family'] = 'Helvetica'

# 生成时间向量
t = np.linspace(0.2, 2, 10)

# 各条折线的数据
y_vectors = [
    [-5.79195, -4.566333333, -2.126866667, -2.3952, -6.8725, 2.41475, 3.8205, -2.12125, -3.50425, -3.79925],
    [-6.798, -6.11575, -0.3805, 0.757, 2.5286, 3.210966667, 1.76345, 7.624666667, 10.83766667, 5.35325],
    [-4.30875, 2.62725, 4.3986, 5.571625, 6.084271429, 6.249, 4.051166667, 1.3405, 4.58725, 4.5825],
    [-12.005, -11.56675, -2.11605, 1.27434, 9.5015, 5.4386, 0.745775, 1.33075, 0.313276667, 0],
    [0, 0, 0, 7.42555, 9.638375, 4.5009, 3.3252, 0.96305, -1.457666667, -2.7115],
    [-1.105, 6.4205, 6.345935, 9.927333333, 14.91591667, 15.42230769, 11.6841, 6.8436, 0.461, 0],
    [0, 0, 0, 5.008666667, 7.846222222, 13.12633333, 17.11625, 10.80685714, 8.489, 6.2345],
    [0, 0, -7.0855, 0.576133333, 6.162166667, 9.678, 8.92675, 9.6612, 6.292, 6.043333333],
    [-10.81833333, -8.249333333, -7.152666667, 2.3403, 9.710571429, 8.974, 8.866714286, 5.8352, 6.962, 4.6875],
    [-10.8735, -0.25665, 2.10022, 6.00925, 7.5926, 7.9892, 17.225, 14.1664, 5.61575, 2.412]
]

# 计算声压级
def calculate_SPL(y_vector):
    delta_E_dB = y_vector + 1.053
    k = 10 ** (delta_E_dB / 20)
    normalized_voltage = k * 0.0025

    V_ref = 1.2
    mic_sensitivity_db = -42
    P_ref = 20e-6

    V_signal = normalized_voltage * V_ref
    mic_sensitivity_linear = 10 ** (mic_sensitivity_db / 20)
    P_signal = V_signal / mic_sensitivity_linear

    SPL = 20 * np.log10(P_signal / P_ref)
    return SPL

SPLs = [calculate_SPL(np.array(y_vector)) for y_vector in y_vectors]

# 将所有数据合并到一个矩阵中
data = np.array(SPLs).T

# 绘制箱线图
fig, ax = plt.subplots(figsize=(12, 7))
n_categories = data.shape[1]
# 分类与宽度设置
group_gap = 0
box_gap = 0
box_width = 8
colors = ['#3c7ba4'] # 您可以使用十六进制RGB颜色代码
# 绘制箱线图
for i in range(n_categories):
    box_data = data[:, i]
    pos = i * (n_categories + group_gap)

    mean = np.mean(box_data)
    std_dev = np.std(box_data)

    print(f"Category {i+1} - Mean: {mean}, Std Dev: {std_dev}")
        
    # 绘制填充颜色的箱线图
    box = ax.boxplot(box_data, positions=[pos], whiskerprops=dict(linestyle='--', linewidth=2),
                    capprops=dict(linewidth=2),  # 设置盖帽的宽度
                    boxprops=dict(linewidth=2, edgecolor="black"),  # 设置箱体边缘的宽度和颜色
                    medianprops=dict(linewidth=2, color="red"),  # 设置中位数线的宽度和颜色
                    widths=box_width,patch_artist=True,flierprops=dict(markerfacecolor='none', marker='o', markeredgecolor="#3c7ba4",markeredgewidth=2, markersize=10))
        
    # 设置箱线图颜色和中间线粗细、颜色
    box['boxes'][0].set_facecolor(colors[0])
    box['medians'][0].set_color('black')
    box['medians'][0].set_linewidth(3)

    # 添加分类之间的竖直虚线
    if 0 < i < n_categories:
        dashed_line_pos = i * n_categories - box_width / 2 - 0.8
        ax.axvline(dashed_line_pos, linestyle='--', color='grey', linewidth=3)

# 设置x轴刻度标签
x_tick_positions = [i * (n_categories + group_gap) for i in range(n_categories)]
x_tick_labels = [str(i+1) for i in range(n_categories)]

ax.set_xticks(x_tick_positions)
ax.set_xticklabels(x_tick_labels)

# 设置左右两侧坐标轴距离
left_margin = x_tick_positions[0] - 6
right_margin = x_tick_positions[-1] + 6
ax.set_xlim(left_margin, right_margin)

# 添加图例
#legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=f'Category {i+1}') for i, color in enumerate(colors)]
#ax.legend(handles=legend_elements, loc='upper right', fontsize='small', ncol=2)

# 设置坐标轴的宽度
ax.spines['top'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)

# 添加横纵坐标标签
plt.xlabel('Number of bats', fontsize=38)
plt.ylabel('SPL (dB)', fontsize=38)

# 设置刻度字体大小
ax.tick_params(axis='both', which='major',direction='in', labelsize=30)
ax.tick_params(axis='x', which='major', width=3, length=8)
ax.tick_params(axis='y', which='major', width=3, length=8)

# 保存图像
plt.savefig('1-10_bats_SPL.jpg', dpi=300, bbox_inches='tight')
#plt.savefig('1-10_bats_SPL.eps', dpi=300, format='eps')

# 显示图形
plt.show()

# 计算每一列之间的显著性差异
p_values = {}
for i in range(data.shape[1]):
    for j in range(i + 1, data.shape[1]):
        _, p_value = ttest_ind(data[:, i], data[:, j], equal_var=False)
        p_values[(i + 1, j + 1)] = p_value

# 筛选出p<0.05对应的列数和p值
significant_pairs = {pair: p_value for pair, p_value in p_values.items() if p_value < 0.05}

# 打印p<0.05对应的列数和p值
for pair, p_value in significant_pairs.items():
    print(f"Columns {pair[0]} and {pair[1]}: p-value = {p_value}")
