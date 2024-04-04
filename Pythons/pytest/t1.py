import pandas as pd
import matplotlib.pyplot as plt

# 假设有两列数据，分别是 x 和 y 坐标
data = {'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 15, 25, 30]}

df = pd.DataFrame(data)

# 画出散点图
plt.scatter(df['x'], df['y'])

# 添加颜色映射，例如根据 y 值的大小来映射颜色
plt.scatter(df['x'], df['y'], c=df['y'], cmap='viridis')

# 添加颜色条
plt.colorbar()

# 设置坐标轴标签
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 设置图形标题
plt.title('Scatter Plot with Color Mapping')

# 显示图形
plt.show()
