import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib import cm

rng = np.random.RandomState()

x = np.linspace(0,9,num=10)
y = rng.randint(0,10,10)
print(y)

f = interpolate.interp1d(x,y)

xnew = np.linspace(0,9,20)
ynew = f(xnew)
print(ynew)