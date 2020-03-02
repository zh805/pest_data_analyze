# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Fixing random state for reproducibility
np.random.seed(19680801)


for i in range(10):
    xs = np.random.randint(50)
    ys = np.random.randint(25)
    zs = np.random.randint(6)
    ax.scatter(xs, ys, zs, marker='d', s=200, c='gray', alpha=0.2)


# ax.scatter(xs,ys,zs,marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
