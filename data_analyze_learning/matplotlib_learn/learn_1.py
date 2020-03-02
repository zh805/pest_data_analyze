#%%
import matplotlib.pyplot as plt 
import numpy as np 
# %% 
# %matplotlib inline
x = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
fig.savefig('test_1.png')
# %%
from IPython.display import Image
Image('test_1.png')
# %%
fig.canvas.get_supported_filetypes()

# %%
fig ,ax = plt.subplots(2)
ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))

# %%
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), linestyle='solid')
ax.plot(x, np.sin(x-1), linestyle='dashed')
ax.plot(x, np.sin(x-2), linestyle='dashdot')
ax.plot(x, np.sin(x-3))
ax.plot(x, np.sin(x-4));
# ax.plot(x, np.cos(x))
# ax.plot(x, np.tan(x))
# ax.plot(x, np.log(x))
# %%
# plt.style.use('classic')
rng = np.random.RandomState(0)
x = np.linspace(0,10,500)
y = np.cumsum(rng.randn(500,6), 0)
plt.plot(x,y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
# %%
import seaborn as sns
sns.set()
plt.plot(x,y)
plt.legend('ABCDEF', ncol=2, loc='lower left');

# %%
