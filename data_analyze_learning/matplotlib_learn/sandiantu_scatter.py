# 面向对象绘制散点图

import numpy as np 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Scatter')

plt.show()

