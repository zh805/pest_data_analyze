# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
# import seaborn

# seaborn.set()
# 可选图片风格
print(plt.style.available)

# 设定画图风格
plt.style.use('fivethirtyeight')
fig = plt.figure()
ax = plt.axes(projection='3d')

# Fixing random state for reproducibility
# np.random.seed(19680801)
# rng = np.random.RandomState(0)
# xs = rng.randint(0, 50, size=30)
# ys = rng.randint(0, 25, size=30)
# zs = rng.randint(0, 6, size=30)

# 测试数据
# xs = np.array([2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48,
#                 2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48,
#                 2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48])

# ys = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 
#                 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 
#                 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23])

# zs = np.array([1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5,
#                 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5,
#                 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5])


x1 = np.array([2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48])
y1 = np.array([2,2,2,2,2,12,12,12,12,12,23,23,23,23,23])
z1 = np.array([1]*15)
z2 = np.array([3]*15)
z3 = np.array([5]*15)

ax.scatter3D(x1, y1, z1, c='green', marker='d', s=200)
ax.scatter3D(x1, y1, z2, c='red', marker='d', s=200)
ax.scatter3D(x1, y1, z3, c='blue', marker='d', s=200)

# ax.scatter(xs, ys, zs, marker='d', s=150, c='blue',label='OITD-PI')

# ax.set_xlabel('粮仓长', fontproperties='SimHei', fontsize=10)
# ax.set_ylabel('粮仓宽', fontproperties='SimHei', fontsize=10)
# ax.set_zlabel('粮仓高', fontproperties='SimHei', fontsize=10)
# ax.set_title('采集终端部署位置示意图', fontproperties='SimHei', fontsize=12)

ax.set_xticks(np.linspace(0,50,11))
ax.set_xticklabels( ('0', '5', '10', '15', '20',  '25',  '30',  '35', '40', '45', '50'))
ax.set_yticks(np.linspace(0,25,6))
ax.set_yticklabels( ('0', '5', '10', '15', '20','25'))
ax.set_zticks(np.linspace(6,0,7))
ax.set_zticklabels( ('0', '1', '2', '3', '4', '5','6', '7'))
# ax.set(xlim=(0,50), ylim=(0,25), zlim=(0,6), xlabel='x', ylabel='y', zlabel='z', title='cang')
ax.legend()
# plt.annotate(r'$\mu=100$', xy=(2,1), xytext=(3,1.5), arrowprops=dict(facecolor='black', shrink=0.1,width=2))

plt.show()
