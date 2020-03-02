import pandas as pd 
import numpy as np 

# %%
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0,10,4))
ser

# %%
df = pd.DataFrame(rng.randint(0,10,(3,4)), columns=['A','B','C','D'])
df

# %%
np.exp(ser)

# %%
np.sin(df*np.pi/4)

# %%
ser_2 = pd.Series([3,4,5], index=[3,4,5])
ser.add(ser_2, fill_value=0)

# %%
