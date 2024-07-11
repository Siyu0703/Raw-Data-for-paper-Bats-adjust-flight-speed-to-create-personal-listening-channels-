# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:19:59 2024

@author: cattree
"""
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy.interpolate import CubicSpline
import matplotlib
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
# 设定起始点、中间点和结束点

points = [
    [(0, 3, 0), (-1.5, 1.5, 0.5), (-1, 0.1, 1)],
    [(0.5, 2.9, 0), (1.5, 1.4, -0.5), (1.5, 0, 0.7)],
    [(-0.5, 2.7, 0), (-0.7, 1.2, 1.5), (-1.5, 0.3, 0.7)],
    [(1, 2.9, 0), (1.6, 1.4, -0.3), (0, 0.2, -1)],
    [(-1, 2.8, 0), (0, 1.3, -0.3), (-1.2, 0.2, 0.8)],
    [(1.5, 2.7, 0.2), (1.5, 1.35, 1.2), (-0.5, 0.3, 1.3)],
    [(-1.5, 3, 0.2), (-1.6, 1.5, 1.1), (-1.3, 0.4, 1.2)],
    [(1.8, 2.9, 0.2), (0, 1.45, -0.3), (-0.8, 0.5, 0.8)],
    [(-1.7, 2.8, 0.2), (-1.8, 1.4, 1), (-1.2, 0.3, 0.9)],
    [(0.3, 2.6, 0.2), (1.3, 1.3, -0.2), (1.6, 0, 0.6)]
]

# 生成平滑轨迹函数
def generate_smooth_line(start, middle, end, num_points=100):
    x = np.array([start[0], middle[0], end[0]])
    y = np.array([start[1], middle[1], end[1]])
    z = np.array([start[2], middle[2], end[2]])

    t = np.linspace(0, 1, 3)
    t_fine = np.linspace(0, 1, num_points)
    
    cs_x = CubicSpline(t, x)
    cs_y = CubicSpline(t, y)
    cs_z = CubicSpline(t, z)
    
    x_smooth = cs_x(t_fine)
    y_smooth = cs_y(t_fine)
    z_smooth = cs_z(t_fine)
    
    return np.vstack((x_smooth, y_smooth, z_smooth)).T

# 生成10组平滑轨迹
lines = []
for start, middle, end in points:
    line = generate_smooth_line(start, middle, end)
    lines.append(line)

# 保存坐标到JSON文件
with open('smooth_lines.json', 'w') as f:
    json.dump([line.tolist() for line in lines], f)

print("Smooth coordinates have been saved to 'smooth_lines.json'.")

# 可视化
# 设置图片的尺寸（宽度和高度，以厘米为单位）
width_cm = 5.5  # 宽度：25厘米
height_cm = 3.78  # 高度：12.5厘米

# 将厘米转换为英寸（1英寸 = 2.54厘米）
width_inch = width_cm / 2.54
height_inch = height_cm / 2.54

# 创建一个新的图形
fig = plt.figure(figsize=(width_inch, height_inch))# 调整图形大小，比例为长方形
ax = fig.add_subplot(111, projection='3d')

# 设置三维坐标的坐标平面为白色
ax.xaxis.pane.set_facecolor('white')
ax.yaxis.pane.set_facecolor('white')
ax.zaxis.pane.set_facecolor('white')

# 如果需要取消平面的网格线，可以设置透明度为0
ax.xaxis.pane.set_alpha(0.7)
ax.yaxis.pane.set_alpha(0.7)
ax.zaxis.pane.set_alpha(0.7)

# 获取颜色循环
colors = plt.cm.tab10(np.linspace(0, 1, len(lines)))

# 绘制每一条平滑曲线
for line, color in zip(lines, colors):
    ax.plot(line[:, 0], line[:, 1], line[:, 2], linewidth=1, color=color)
    
    # 随机选取10-15个点并用圆圈标记
    num_pulses = np.random.randint(5, 10)
    pulse_indices = np.random.choice(len(line), num_pulses, replace=False)
    ax.plot(line[pulse_indices, 0], line[pulse_indices, 1], line[pulse_indices, 2], 'o', markersize=1, color=color)

ax.set_xlabel('X (m)', fontsize=6)
ax.set_ylabel('Y (m)', fontsize=6)
#ax.set_zlabel('Z (m)', fontsize=6)

# 设置长方体比例
ax.set_box_aspect([4, 6, 4])  # 长方体的比例，2:1:1
# 设置视角 (方位角，俯仰角)
ax.view_init(azim=-20, elev=10)

# 设置刻度字体大小
ax.tick_params(axis='x', labelsize=5.5, width=0.5, length=1)
ax.tick_params(axis='y', labelsize=5.5, width=0.5, length=1)
ax.tick_params(axis='z', labelsize=5.5, width=0.5, length=1)

# 设置自定义刻度
x_ticks = [-2, 0, 2]
y_ticks = [0, 1, 2, 3]
z_ticks = [-1.5, 0, 1.5]

ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.set_zticks(z_ticks)

# 设置坐标轴范围
ax.set_xlim([-2, 2])  # X 轴范围
ax.set_ylim([0, 3])  # Y 轴范围
ax.set_zlim([-1.5, 1.5])  # Z 轴范围

# 调整坐标轴标签与坐标轴之间的距离
ax.xaxis.labelpad = -12 # x轴标签与x轴之间的距离，单位为点（points）
ax.yaxis.labelpad = -12  # y轴标签与y轴之间的距离，单位为点（points）
ax.zaxis.labelpad = -12  # y轴标签与y轴之间的距离，单位为点（points）

# 调整刻度标签与坐标轴之间的距离
ax.tick_params(axis='x', pad=-5)  # x轴刻度标签与x轴之间的距离，单位为点（points）
ax.tick_params(axis='y', pad=-5)  # y轴刻度标签与y轴之间的距离，单位为点（points）
ax.tick_params(axis='z', pad=-5)

# 设置坐标轴的线宽
for spine in ax.spines.values():
    spine.set_linewidth(1)

# 添加XOY平面、XOZ平面和YOZ平面的投影
for line, color in zip(lines, colors):
    # 绘制XOY平面的投影
    ax.plot(line[:, 0], line[:, 1], -1.5 * np.ones_like(line[:, 2]), linewidth=0.5, color=color, alpha=0.5, linestyle='--')
    # 绘制XOZ平面的投影
    ax.plot(line[:, 0], 3 * np.ones_like(line[:, 1]), line[:, 2], linewidth=0.5, color=color, alpha=0.5, linestyle='--')
    # 绘制YOZ平面的投影
    ax.plot(-2 * np.ones_like(line[:, 0]), line[:, 1], line[:, 2], linewidth=0.5, color=color, alpha=0.5, linestyle='--')

# 调整子图的边距，使图形充满整个画布
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # 将边距调整为0

plt.savefig('10只轨迹_平滑.jpg', dpi=600, format='jpg')
print("sucessful")
plt.show()
