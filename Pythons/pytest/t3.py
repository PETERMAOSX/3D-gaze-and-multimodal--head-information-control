import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# 生成随机聚类数据
n_samples = 600
n_features = 2
n_clusters = 4

X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)

# 创建DataFrame
df = pd.DataFrame(data=X, columns=['X1', 'X2'])
df['cluster'] = y

# 打印数据的前几行
print(df.head())

# 画出聚类结果
plt.scatter(df['X1'], df['X2'], c=df['cluster'], cmap='viridis', edgecolors='k', marker='o')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Randomly Generated Clustering Data')
plt.show()
