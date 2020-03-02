import numpy as np 
#%%
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))
# %%
print(x1.ndim)
print(x2.ndim)
print(x3.ndim)
print(x3.shape)
print(x3.size)
print(x3.dtype)
# %%
x1
x1[0]
# %%
x2[0]
x2[0,0]
# %%
x2[2,-1]

# %%
x1[0]

# %%
x1[:8]

# %%
x1[::2]

# %%
x1[5::-2]

# %%
x2

# %%
x2[:2,:3]

# %%
x2[:3, ::2]

# %%
x2_sub_copy = x2[:2, :2].copy()
x2_sub_copy
# %%
grid = np.arange(0,10).reshape(2,5)
grid
# %%
x1[:,np.newaxis]
x1
# %%
# x1 = np.concatenate(x1,[1,23,3])
x1
# %%
a = np.array([1,2,3])
b = np.array([1,2,3])
np.concatenate([a,b])
# %%
np.vstack([a,b])

# %%
np.hstack([a,b])

# %%
x1

# %%
x1 + 3

# %%
x1 ** 2

# %%
theta = np.linspace(0, np.pi, 3)
theta
np.sin(theta)
# %%
x = np.arange(5)
y = np.empty(5)
np.multiply(x,10,out=y)
y
# %%
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)
# %%
x = np.arange(1,6)
np.add.reduce(x)

# %%
np.multiply.reduce(x)

# %%
np.add.accumulate(x)

# %%
x = np.linspace(0,5,50)
y = np.linspace(0,5,50)[:,np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y*x)*np.cos(x)
import matplotlib.pyplot as plt 
plt.imshow(z, origin='lower', extent=[0,5,0,5], cmap='viridis')
plt.colorbar()
# %%
bin(42)

# %%
mean = [0,0]
cov = [[1,2],[2,5]]
X = np.random.multivariate_normal(mean,cov,100)
X.shape

# %%
import seaborn; seaborn.set()

plt.scatter(X[:,0], X[:,1])

# %%
indices = np.random.choice(X.shape[0], 20, replace=False)
indices

# %%
selection = X[indices]
selection.shape

# %%
plt.scatter(X[:,0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0],selection[:,1], facecolor='none', edgecolors='b', s=200)

# %%
