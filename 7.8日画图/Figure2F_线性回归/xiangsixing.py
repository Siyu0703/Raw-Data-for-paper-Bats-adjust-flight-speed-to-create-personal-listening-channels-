import pandas as pd
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

# 读取Excel文件
df = pd.read_excel('b_d.xlsx')

# 获取两列数据
x = df['duration'].values.reshape(-1, 1)
y = df['bandwidth'].values

# 计算相关系数
corr_coeff, _ = pearsonr(df['duration'], df['bandwidth'])

# 创建并训练线性回归模型
model = LinearRegression().fit(x, y)

# 计算确定系数 (R²)
r_squared = model.score(x, y)

# 输出结果
print("相关系数:", corr_coeff)
print("确定系数 (R²):", r_squared)


