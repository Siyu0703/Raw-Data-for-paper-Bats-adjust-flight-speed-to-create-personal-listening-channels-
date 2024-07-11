import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import statsmodels.api as sm
import matplotlib
import seaborn as sns
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

# 示例数据（替换成你的数据）
file_path = 'b_d.xlsx'  # Update with the actual file path
data = pd.read_excel(file_path)
# 绘制散点图
x=data['duration']
y=data['bandwidth']
plt.figure(figsize=(12,7))
plt.scatter(x, y, label='Data Points', color='#3c7ba4', s=200)

# 进行线性回归分析
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# 计算回归线的预测值
regression_line = [slope * xi + intercept for xi in x]

# 绘制回归线，设置为黑色虚线
plt.plot(x, regression_line, color='#C04851', linestyle='-', label='Linear Regression',linewidth=3)
# 设置坐标轴的线宽
ax = plt.gca()  # 获取当前图像的坐标轴

# 添加方程式和p值文本
equation_text = f'R={0.98}\nR²={0.964}\nP < {0.001}'
plt.text(0.08, 0.93, equation_text, horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, fontsize=30)

# 添加标签和标题
plt.xlabel('Mean FM duration (ms)', fontsize=38)
plt.ylabel('Mean bandwidth (kHz)', fontsize=38)
#plt.title('Scatter Plot with Linear Regression', fontsize=14)

# 设置坐标轴刻度在内侧，并设置刻度字体大小
plt.tick_params(direction='in', labelsize=30)
#plt.tick_params(width=2)
# 设置坐标轴的宽度

ax.spines['top'].set_linewidth(3)    # 设置顶部脊线的宽度
ax.spines['right'].set_linewidth(3)  # 设置右侧脊线的宽度
ax.spines['left'].set_linewidth(3)   # 设置左侧脊线的宽度
ax.spines['bottom'].set_linewidth(3) # 设置底部脊线的宽度

# 设置x轴和y轴刻度线的线宽
ax.tick_params(axis='x', which='major', width=3,length=8)  # 设置x轴主刻度线的线宽为2
ax.tick_params(axis='y', which='major', width=3,length=8)  # 设置y轴主刻度线的线宽为2

'''
# 获取当前的轴并设置边框线宽
ax = plt.gca()
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
    '''
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)

# 打印回归分析的结果
print(f"斜率 (Slope): {slope}")
print(f"截距 (Intercept): {intercept}")
print(f"相关系数 (R-value): {r_value}")
print(f"p-value: {p_value}")
print(f"标准误差 (Standard Error): {std_err}")

plt.savefig('bandwidth_FMduration.jpg', dpi=300, bbox_inches='tight')
'''

#保存图像
plt.savefig('bandwidth_FMduration.svg', dpi=300, bbox_inches='tight', format='svg')
plt.savefig('bandwidth_FMduration.eps', dpi=300, bbox_inches='tight', format='eps')
'''
# 显示图形
plt.show()