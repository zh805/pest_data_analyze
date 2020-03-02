import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(0)
mu, sigma = 100, 20
a = np.random.normal(mu, sigma, size=100)

plt.hist(a, 30, normed=0, histtype='stepfilled', facecolor='b', alpha=0.75)
# 30区间个数   normed:0个数  1频率
plt.title('Histogram')

plt.show()

