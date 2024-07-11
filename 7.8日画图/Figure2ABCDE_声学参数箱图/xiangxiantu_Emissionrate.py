
# FM duration箱线图
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

# 设置全局线条宽度
plt.rc('lines', linewidth=2)  # 将线条宽度设置为2
# 从Excel文件读取数据
df = pd.read_excel('1s脉冲数.xlsx', engine='openpyxl')
# 获取不同分类的数量
n_categories = df['Category'].nunique()

# 分类与宽度设置
group_gap = 0
box_gap = 0
box_width = 8

# 定义颜色和图例标签

colors = ['#3c7ba4'] # 您可以使用十六进制RGB颜色代码
r_mean=[]
# 绘制箱线图
fig, ax = plt.subplots(figsize=(12, 7))

for i, (category, cat_df) in enumerate(df.groupby('Category')):
    # 对于每个类别，分别计算箱线图的位置
   box_data = cat_df['Value']
   pos = i * (n_categories + group_gap)
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
                    capprops=dict(linewidth=2),  # 设置盖帽的宽度
                    boxprops=dict(linewidth=2, edgecolor="black"),  # 设置箱体边缘的宽度和颜色
                    medianprops=dict(linewidth=2, color="red"),  # 设置中位数线的宽度和颜色
                    widths=box_width,patch_artist=True,flierprops=dict(markerfacecolor='none', marker='o', markeredgecolor="#3c7ba4",markeredgewidth=2, markersize=10))
        
   # 设置箱线图颜色和中间线粗细、颜色
   box['boxes'][0].set_facecolor(colors[0])
   box['medians'][0].set_color('black')
   box['medians'][0].set_linewidth(3)
        
       
    # 添加分类之间的竖直虚线
   if 0<i < n_categories:
        dashed_line_pos = i * n_categories-box_width/2-0.8
        ax.axvline(dashed_line_pos, linestyle='--', color='grey',linewidth='3')   
  
# 设置x轴刻度标签
x_tick_positions = []
x_tick_labels = []

for i, category in enumerate(df['Category'].unique()):
    cat_center = i * (n_categories + group_gap)
    x_tick_positions.append(cat_center)
    
#自定义分类
x_tick_labels= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

ax.set_xticks(x_tick_positions)
ax.set_xticklabels(x_tick_labels)


# 设置左右两侧坐标轴距离
left_margin = x_tick_positions[0] - 6  # 1.5是自定义的距离，可以根据需要调整
right_margin = x_tick_positions[-1]+6  # 1.5是自定义的距离，可以根据需要调整
ax.set_xlim(left_margin, right_margin)

'''
# 添加显著性线的函数
def add_significance_line(ax, x1, x2, y_max, significance_label, y_offset=0.05):
    ax.plot([x1, x1, x2, x2], [y_max, y_max + y_offset, y_max + y_offset, y_max], lw=1.5, c='k')
    ax.text((x1 + x2) / 2, y_max + y_offset, significance_label, ha='center', va='bottom', color='k', fontsize=14)

# 添加显著性线
y_max_a = 10
add_significance_line(ax, 1,10, y_max_a, 'p<0.05')
y_max_a = 11
add_significance_line(ax, 1,50, y_max_a, 'p<0.05')
'''
# 添加图例
#legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(colors, labels)]

# 将图例放在图像的右侧
#legend = ax.legend(handles=legend_elements, loc='lower left', bbox_to_anchor=(0.6,1), frameon=False,ncol=2)
'''
#去掉右侧和上侧的边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
'''
# 设置坐标轴的宽度
ax.spines['top'].set_linewidth(3)    # 设置顶部脊线的宽度
ax.spines['right'].set_linewidth(3)  # 设置右侧脊线的宽度
ax.spines['left'].set_linewidth(3)   # 设置左侧脊线的宽度
ax.spines['bottom'].set_linewidth(3) # 设置底部脊线的宽度

# 设置y轴的范围
#plt.ylim(3, 10)  # CFduration
# 添加横纵坐标标签
plt.xlabel('Number of bats', fontsize=38)
plt.ylabel('Emission rate (Hz)', fontsize=38)

# 设置刻度字体大小
ax.tick_params(axis='both', which='major',direction='in', labelsize=30)
# 设置x轴和y轴刻度线的线宽
ax.tick_params(axis='x', which='major', width=3, length=8)  # 设置x轴主刻度线的线宽为2
ax.tick_params(axis='y', which='major', width=3, length=8)  # 设置y轴主刻度线的线宽为2
#保存图像
plt.savefig('Emission rate.jpg', dpi=300, bbox_inches='tight')
#plt.savefig('Emission rate.eps', dpi=300, format='eps')
'''
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# 示例：将RGB颜色(255, 0, 0)转换为16进制颜色
hex_color = rgb_to_hex((60, 123,164))
print(hex_color)  # 输出: #ff0000
'''
# 显示图形
plt.show()
