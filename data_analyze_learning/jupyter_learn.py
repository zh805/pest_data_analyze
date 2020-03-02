#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 
# %%
#%timeit L = [n**2 for n in range(100)]
# %%
#%%timeit
l = []
for n in range(100):
    l.append(n**2)

# %%
# %lsmagic?
# %%
import math
math.sin(2)

# %%
math.cos(2)

# %%
print(In)

# %%
print(In[-1])

# %%
print(In(9))

# %%
print(Out[-1])

# %%
print(Out[0])

# %%
print(Out[2])

# %%
print(_)

# %%
print(__)

# %%
%%timeit
math.sin(2)**2 + math.cos(2)**2
# %%
41 in Out

# %%
%history -n 1-4

# %%
!ls

# %%
!pwd

# %%
!echo "ksljlkdjf"

# %%
contents = !ls 
print(contents)

# %%
type(contents)

# %%
%timeit sum(range(100))

# %%
%time?
# %%

# %%


# %%
