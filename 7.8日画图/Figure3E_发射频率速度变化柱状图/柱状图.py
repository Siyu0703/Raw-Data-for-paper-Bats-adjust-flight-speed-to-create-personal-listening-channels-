# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:31:37 2024

@author: cattree
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as font_manager
from matplotlib import rcParams
import matplotlib.lines as mlines

# 路径替换为你Helvetica.ttf字体文件的实际路径
font_path = 'D:/app/helvetica/HelveticaTTF/Helvetica/Helvetica.ttf'

# 添加这个字体路径
font_manager.fontManager.addfont(font_path)
# 设置全局字体
rcParams['font.family'] = 'Helvetica'
# 如果matplotlib没有识别到Helvetica，可以使用下面的方式设置
# rcParams['font.sans-serif'] = 'Helvetica'
# 设置全局字体为Helvetica
rcParams['font.family'] = 'Helvetica'

# 设置全局线条宽度
plt.rc('lines', linewidth=2)  # 将线条宽度设置为2

# 数据
'''
change = {
    'increase frequency': [78.6/100, 18.8/100, 2.6/100],
    'decrease frequency': [4.8/100, 6.7/100, 88.5/100],
}

other = {
    'increase frequency': [20/100, 80/100, 0/100],
    'decrease frequency': [83.3/100, 16.7/100, 0/100],
}
'''

change = {
    'increase frequency': [78.6, 18.8, 2.6],
    'decrease frequency': [4.8, 6.7, 88.5],
}

other = {
    'increase frequency': [2/10*100, 0, 8/10*100],
    'decrease frequency': [8/11*100, 0, 3/11*100],
}

# 设置
labels = ['Increase frequency', 'Decrease frequency']
factors = ['Increase speed', 'Maintain speed', 'Decrease speed']
colors = ['#0F72B7', '#CC5A2D', '#AD80B7']  # 分别为蓝色、橙色和绿色
category_names = ['change', 'other']

x = np.arange(len(labels))  # 标签位置
width = 0.3  # 柱状图的宽度

fig, ax = plt.subplots(figsize=(9, 7.8))

# 大类1
rects1 = ax.bar(x - width/2-0.025, [val[0] for val in change.values()], width, label=factors[0], color=colors[0])
rects2 = ax.bar(x - width/2-0.025, [val[1] for val in change.values()], width, bottom=[val[0] for val in change.values()], label=factors[1], color=colors[1])
rects3 = ax.bar(x - width/2-0.025, [val[2] for val in change.values()], width, bottom=np.array([val[0] for val in change.values()]) + np.array([val[1] for val in change.values()]), label=factors[2], color=colors[2])

# 大类2
rects4 = ax.bar(x + width/2+0.025, [val[0] for val in other.values()], width, label=factors[0], color=colors[0])
rects5 = ax.bar(x + width/2+0.025, [val[1] for val in other.values()], width, bottom=[val[0] for val in other.values()], label=factors[1], color=colors[1])
rects6 = ax.bar(x + width/2+0.025, [val[2] for val in other.values()], width, bottom=np.array([val[0] for val in other.values()]) + np.array([val[1] for val in other.values()]), label=factors[2], color=colors[2])

# 添加文本和标签
ax.set_ylabel('Percentage (%)', fontsize=29)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=23)

# 在每个大类上方添加大类标签
for i in range(len(labels)):
    ax.text(i - width+0.125, 105, 'Change', ha='center', va='center', fontweight='bold', fontsize=21)
    ax.text(i + width-0.125, 105, 'Other', ha='center', va='center', fontweight='bold', fontsize=21)

# 移除上面和右侧的坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 设置坐标轴宽度
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)

ax.set_ylim([0, 105])  # Y 轴范围

# 设置刻度字体大小，方向和长度
ax.tick_params(axis='x', labelsize=24, width=3, length=8, direction='in')
ax.tick_params(axis='y', labelsize=24, width=3, length=8, direction='in')

# 添加图例，ncol参数用于设置图例列数
#ax.legend(factors, loc='upper center', bbox_to_anchor=(0.7, 1.15), ncol=3, fontsize=20, frameon=False)
legend_handles = [
    mlines.Line2D([], [], color='#0F72B7', marker='s', linestyle='None', markersize=20, label='Increase speed'),
    mlines.Line2D([], [], color='#CC5A2D', marker='s', linestyle='None', markersize=20, label='Maintain speed'),
    mlines.Line2D([], [], color='#AD80B7', marker='s', linestyle='None', markersize=20, label='Decrease speed')
]
ax.legend(handles=legend_handles, loc='upper center', bbox_to_anchor=(0.45, 1.17), ncol=3, fontsize=21, frameon=False, handletextpad=-0.2, columnspacing=1)

fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# 添加分类之间的虚线
ax.axvline(x=0.5, color='gray', linestyle='--', linewidth=3)

plt.savefig('percentage.jpg', dpi=300, bbox_inches='tight')

plt.show()
