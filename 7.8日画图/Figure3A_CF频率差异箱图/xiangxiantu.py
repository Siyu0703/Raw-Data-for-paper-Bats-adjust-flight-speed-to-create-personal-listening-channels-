# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:57:10 2024

@author: cattree
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import matplotlib as mpl
from matplotlib import rcParams
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from matplotlib.ticker import FormatStrFormatter
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

# 从Excel文件读取数据
df = pd.read_excel('overlap2.xlsx', engine='openpyxl')
# 获取不同分类的数量
n_categories = df['Category'].nunique()

# 分类与宽度设置
group_gap = 2
box_gap =1
box_width = 5.5

# 定义颜色和图例标签

colors = ['#3c7ba4', '#B04F48'] # 您可以使用十六进制RGB颜色代码
r_mean=[]
# 绘制箱线图
fig, ax = plt.subplots(figsize=(18, 12))
# 初始化用于收集dashed_line_pos的列表
dashed_line_positions = []
for i, (category, cat_df) in enumerate(df.groupby('Category')):
    for j, (subcategory, subcat_df) in enumerate(cat_df.groupby('Subcategory')):
      box_data = subcat_df['Value']
      pos = i * (n_categories + group_gap) + j * (box_width + box_gap)
      # 使用numpy计算均值
      mean = np.mean(box_data)
      r_mean.append(mean)

      # 使用numpy计算标准差
      std_dev = np.std(box_data)
      r_std_dev=round(std_dev,2)

      print("均值: ", mean)
      print("标准差: ", std_dev)
        
      # 绘制填充颜色的箱线图
      box = ax.boxplot(box_data, positions=[pos], whiskerprops=dict(linestyle='--', linewidth=2),
                       capprops=dict(linewidth=3),  # 设置盖帽的宽度
                       boxprops=dict(linewidth=3, edgecolor="black"),  # 设置箱体边缘的宽度和颜色
                       medianprops=dict(linewidth=3, color="red"),  # 设置中位数线的宽度和颜色
                       widths=box_width,patch_artist=True,flierprops=dict(markerfacecolor='none', marker='o', markeredgecolor=colors[j],markeredgewidth=2, markersize=10))
           
      # 设置箱线图颜色和中间线粗细、颜色
      box['boxes'][0].set_facecolor(colors[j])
      box['medians'][0].set_color('black')
      box['medians'][0].set_linewidth(4)
        
       
    # 添加分类之间的竖直虚线
    if i < n_categories - 1:
        dashed_line_pos = (i + 1) * (n_categories + group_gap) - group_gap / 2-2.5
        ax.axvline(dashed_line_pos, linestyle='--', color='grey',linewidth='4') 
        dashed_line_positions.append(dashed_line_pos)  # 将位置添加到列表中
# 设置x轴刻度标签
x_tick_positions = []
x_tick_labels = []

for i, category in enumerate(df['Category'].unique()):
    n_subcategories = df[df['Category'] == category]['Subcategory'].nunique()
    cat_center = i * (n_categories + group_gap) + (n_subcategories - 1) * (box_width + box_gap) / 2
    x_tick_positions.append(cat_center)
    
#自定义分类
x_tick_labels= ['>2000', '<2000', '<1800','<1600', '<1400', '<1200', '<1000', '<800', '<600', '<400', '<270', '<90']

ax.set_xticks(x_tick_positions)
ax.set_xticklabels(x_tick_labels)


# 设置左右两侧坐标轴距离
left_margin = x_tick_positions[0]-10  # 1.5是自定义的距离，可以根据需要调整
right_margin = x_tick_positions[-1]+10  # 1.5是自定义的距离，可以根据需要调整
ax.set_xlim(left_margin, right_margin)
# 设置右侧Y轴的范围为0到20
ax.set_ylim(-100, 3800)


# 添加显著性线的函数
def add_significance_line(ax, x1, x2, y_max, significance_label, y_offset=30):
    ax.plot([x1, x1, x2, x2], [y_max, y_max + y_offset, y_max + y_offset, y_max], lw=3, c='k')
    ax.text((x1 + x2) / 2, y_max + y_offset-100, significance_label, ha='center', va='bottom', color='k', fontsize=38)

# 添加显著性线
y_max_a = 3500
add_significance_line(ax, 1,4+3, y_max_a, '***')
'''
y_max_a = 2800
add_significance_line(ax, 17-3,17+3, y_max_a, '*')
y_max_a = 2600
add_significance_line(ax, 31-3,31+3, y_max_a, '*')
y_max_a = 2000
add_significance_line(ax, 45-3,45+3, y_max_a, '**')
y_max_a = 2200
add_significance_line(ax, 59-3,59+3, y_max_a, '***')
y_max_a = 2200
add_significance_line(ax, 73-3,73+3, y_max_a, '***')
y_max_a = 1800
add_significance_line(ax, 87-3,87+3, y_max_a, '*')
y_max_a = 2000
add_significance_line(ax, 101-3,101+3, y_max_a, '*')
y_max_a = 1500
add_significance_line(ax, 115-3,115+3, y_max_a, '*')

y_max_a = 1200
add_significance_line(ax, 129-3,129+3, y_max_a, '**')
'''
y_max_a = 2000
add_significance_line(ax, 143-3,143+3, y_max_a, '***')
y_max_a = 1100
add_significance_line(ax, 157-3,157+3, y_max_a, '***')



# 添加图例
labels = ['Specific calls', 'Subsequent calls']
legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(colors, labels)]

# 将图例放在图像的右侧
legend = ax.legend(handles=legend_elements, loc='lower left', bbox_to_anchor=(0.67,0.81), frameon=True,ncol=1,fontsize=28)

# 设置图例背景为白色且不透明
legend.get_frame().set_facecolor('white')
legend.get_frame().set_alpha(1)
legend.get_frame().set_edgecolor('none')  # 移除边框
'''
#去掉右侧和上侧的边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
'''

# 设置坐标轴的宽度
ax.spines['top'].set_linewidth(2)    # 设置顶部脊线的宽度
ax.spines['right'].set_linewidth(2)  # 设置右侧脊线的宽度
ax.spines['left'].set_linewidth(2)   # 设置左侧脊线的宽度
ax.spines['bottom'].set_linewidth(2) # 设置底部脊线的宽度
# 设置y轴的范围
#plt.ylim(3, 10)  # 例如，设置y轴范围为-3到3
#plt.ylim(0, 1330)  # 例如，设置y轴范围为-3到3
# 添加横纵坐标标签
plt.xlabel('CF frequency difference interval (Hz)', fontsize=24)
plt.ylabel('CF frequency difference (Hz)', fontsize=24)
# 设置坐标轴刻度在内侧，并设置刻度字体大小
plt.tick_params(direction='in', labelsize=18)
#plt.tick_params(width=2)
# 设置x轴和y轴刻度线的线宽
ax.tick_params(axis='x', which='major', width=3,length=10)  # 设置x轴主刻度线的线宽为2
ax.tick_params(axis='y', which='major', width=3,length=10)  # 设置y轴主刻度线的线宽为2

#保存图像

plt.savefig('CFfrequencydifference.jpg', dpi=300, bbox_inches='tight')
# plt.savefig('CFfrequencydifference.eps', dpi=300, bbox_inches='tight', format='eps')
# plt.savefig('CFfrequencydifference.png', dpi=300, bbox_inches='tight', format='png')


'''
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# 示例：将RGB颜色(255, 0, 0)转换为16进制颜色
hex_color = rgb_to_hex((173, 128,183))
print(hex_color)  # 输出: #ff0000
'''
# 显示图形
plt.show()
