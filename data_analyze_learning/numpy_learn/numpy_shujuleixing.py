# %%
import numpy as np 

L = list(range(10))
type(L[0])
L2 = [str(c) for c in L]
L2
# %%
np.array([3.14, 4, 5, 6])
np.array([range(i,i+3) for i in [2,4,6]])
# %%
np.zeros(10, dtype=int)

# %%
np.ones((3,5), dtype=float)

# %%
np.full((3,5), 3.14)

# %%
np.arange(0, 20, 2)

# %%
np.linspace(0, 1, 5)

# %%
# np.random.random(3)

# %%
np.random.normal(0,1,(3,3))

# %%
np.random.randint(0, 10, (3,4))

# %%
np.eye(3)

# %%
np.eye(3,4)

# %%
np.empty(3)

# %%
np.zeros((3,3), dtype=np.int_)

# %%
