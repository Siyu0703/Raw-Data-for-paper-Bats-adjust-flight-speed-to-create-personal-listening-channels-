import pandas as pd
import numpy as np
import glob  # 用于文件路径的模式匹配
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np
import glob  # 用于文件路径的模式匹配
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
import matplotlib.pyplot as plt

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
# Excel文件的路径列表，假设所有文件都在同一个目录下
excel_files = glob.glob(r'C:\Users\cattree\Desktop\7.8日画图\Figure3B_CF频率差异分布柱状图\*.xlsx')

# 初始化一个空的列表来存储所有数据
all_data = []

# 遍历每个文件
for file in excel_files:
    # 读取当前Excel文件
    df = pd.read_excel(file, engine='openpyxl')
    # 将DataFrame的所有值转换为一维数组并添加到all_data列表中
    # 使用pd.DataFrame.values.flatten()来扁平化数据，然后用np.concatenate添加到all_data
    all_data.append(df.values.flatten())

# 合并所有数据为一个一维数组，同时移除NaN值
all_data_flat = np.concatenate(all_data)
all_data_clean = all_data_flat[~np.isnan(all_data_flat)]  # 去除NaN值

# 定义区间的边界
#bins = [0,90,270,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000, np.max(all_data_clean)+1]  # 确保包括所有数据
bins = [0,90,270,400,600,800,1000,1200,1400,1600,1800,2000,3000]  # 确保包括所有数据
# 计算每个点的权重，使得权重之和为1，转换为百分比
weights = np.ones_like(all_data_clean) / len(all_data_clean)*100
fig, ax = plt.subplots(figsize=(12, 7))

# 计算直方图的计数和区间边界
counts, bin_edges = np.histogram(all_data_clean, bins=bins)

# 计算总数以便将计数转换为百分比
total_counts = counts.sum()

# 计算每个区间的中点
bin_middles = (bin_edges[:-1] + bin_edges[1:]) / 2

# 计算每个区间的百分比
percentages = (counts / total_counts) * 100

# 输出每个区间的中点和对应的百分比
for middle, percentage in zip(bin_middles, percentages):
    print(f"区间中点: {middle:.2f}, 百分比: {percentage:.2f}%")

# 绘制直方图
plt.hist(all_data_clean, bins=bins, weights=weights, edgecolor='black',color='#3c7ba4', linewidth=2)
plt.xlabel('CF frequency difference interval (Hz)', fontsize=36)
plt.ylabel('Percentage (%)', fontsize=36)

# 设置坐标轴的宽度
ax.spines['top'].set_linewidth(3)    # 设置顶部脊线的宽度
ax.spines['right'].set_linewidth(3)  # 设置右侧脊线的宽度
ax.spines['left'].set_linewidth(3)   # 设置左侧脊线的宽度
ax.spines['bottom'].set_linewidth(3) # 设置底部脊线的宽度
# 设置刻度字体大小
ax.tick_params(axis='both', which='major',direction='in', labelsize=28)
# 设置x轴和y轴刻度线的线宽
ax.tick_params(axis='x', which='major', width=3,length=8)  # 设置x轴主刻度线的线宽为2
ax.tick_params(axis='y', which='major', width=3,length=8)  # 设置y轴主刻度线的线宽为2

plt.savefig('分布.jpg', dpi=300, bbox_inches='tight')
'''
#保存图像
plt.savefig('分布.svg', dpi=300, bbox_inches='tight', format='svg')
plt.savefig('分布.eps', dpi=300, bbox_inches='tight', format='eps')

'''
plt.show()
