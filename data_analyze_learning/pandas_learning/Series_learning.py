# %%
import numpy as np 
import pandas as pd

# %%
data = pd.Series([0,1,2,3])
data

# %%
data.values

# %%
data.index

# %%
data[1]

# %%
area_dict = {'ca':123, 'la':33, 'ny':44}
popu_dict = {'ca':123, 'la':33, 'ny':44}
area = pd.Series(area_dict)
popu = pd.Series(popu_dict)
data = pd.DataFrame({'popu':popu, 'area':area})
data['density'] = data['popu'] / data['area']
data
# %%
data.T
# %%
data.index
# %%
data
# %%
data.columns

# %%
data['area']

# %%
data = [{'a':i, 'b':2*i} for i in range(3)]
pd.DataFrame(data)

# %%
pd.DataFrame(np.random.rand(3,2), index=['a','b','c'], columns=['foo', 'bar'])

# %%
ind = pd.Index([1,2,3])
ind

# %%
ind[1]

# %%
print(ind.size, ind.shape, ind.ndim, ind.dtype)

# %%
data = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
data
# %%
data['b']

# %%
'a' in data

# %%
data['a':'c']

# %%
data[0:2]

# %%
data[(data>1) & (data<3)]

# %%
data[['a','c']]

# %%
data.loc[1]

# %%
data = pd.Series(['a', 'b', 'c'], index=[1,3,5])
data.loc[1]

# %%
data[1]

# %%
data[1:3]

# %%
data.iloc[1]

# %%
