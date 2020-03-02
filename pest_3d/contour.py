import matplotlib.pyplot as plt 
import numpy as np 

def f(x,y):
    return np.sin(x)**10 + np.cos(10 + y * x) * np.cos(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 20, cmap='GnBu')
plt.colorbar()
plt.show()