from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.arange(-5.01, 5.01, 0.25)
y = np.arange(-5.01, 5.01, 0.25)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2+yy**2)
f = interp2d(x, y, z, kind='cubic')

# Now use the obtained interpolation function and plot the result:

xnew = np.arange(-5.01, 5.01, 1e-2)
ynew = np.arange(-5.01, 5.01, 1e-2)
znew = f(xnew, ynew)
ax.scatter(xnew, ynew, znew, marker='d', s=200, c='red',label='OITD-PI')
# plt.plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
plt.show()