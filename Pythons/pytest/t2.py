import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 假设有两列数据，即离散点的 x 和 y 坐标
data = {'x': [1, 2, 2, 3, 3, 3, 4, 4, 5,6,6.2,6.5,6.7,8,10],
        'y': [5, 4, 3, 2, 1, 2, 3, 4, 5,5,6,6,4,3,2]}
from sklearn.datasets import make_blobs

# 生成随机聚类数据
n_samples = 600
n_features = 2
n_clusters = 4

X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)

# 创建DataFrame
df = pd.DataFrame(data=X, columns=['X1', 'X2'])

#df = pd.DataFrame(data)

# 画出分布密度热点图
sns.kdeplot(x=df['x'], y=df['y'], cmap='Reds', fill=True)
sns.scatterplot(x=df['x'],y=df['y'])

# 设置坐标轴标签
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 设置图形标题
plt.title('2D Kernel Density Estimation Plot')

# 显示图形
plt.show()
