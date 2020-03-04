# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
# import seaborn

# seaborn.set()
print(plt.style.available)
# with plt.style.context('seaborn-pastel'): #fivethirtyeight seaborn-pastel seaborn-whitegrid ggplot bmh

plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes(projection='3d')

# Fixing random state for reproducibility
np.random.seed(19680801)

xs = []
ys = []
zs = []

# for i in range(10):
#     xs.append(np.random.randint(50))
#     ys.append(np.random.randint(25))
#     zs.append(np.random.randint(6))
#     # ax.scatter(xs, ys, zs, marker='d', s=200, c='grey', alpha=0.8)

rng = np.random.RandomState(0)
# xs = rng.randint(0, 50, size=30)
xs = np.array([2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48,
                2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48,
                2, 14, 26, 38, 48,2, 14, 26, 38, 48,2, 14, 26, 38, 48])

# ys = rng.randint(0, 25, size=30)
ys = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 
                12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 
                23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23])

# zs = rng.randint(0, 6, size=30)
zs = np.array([1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5,
                1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5,
                1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5])

# ax.scatter3D(xs, ys, zs, c='black', marker='d', s=200)
ax.scatter(xs, ys, zs, marker='d', s=150, c='blue',label='OITD-PI')

ax.set_xlabel('粮仓长', fontproperties='SimHei', fontsize=10)
ax.set_ylabel('粮仓宽', fontproperties='SimHei', fontsize=10)
ax.set_zlabel('粮仓高', fontproperties='SimHei', fontsize=10)
ax.set_title('采集终端部署位置示意图', fontproperties='SimHei', fontsize=12)

# ax.set(xlim=(0,50), ylim=(0,25), zlim=(0,6), xlabel='x', ylabel='y', zlabel='z', title='cang')
ax.legend()
# plt.annotate(r'$\mu=100$', xy=(2,1), xytext=(3,1.5), arrowprops=dict(facecolor='black', shrink=0.1,width=2))

plt.show()
