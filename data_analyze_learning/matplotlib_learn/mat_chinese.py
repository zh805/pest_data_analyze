import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.size'] = '20'

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
plt.ylabel('纵轴：振幅', fontproperties='KaiTi', fontsize=20)
plt.title(r'正弦$y=cos(2\pi x)$', fontproperties='YouYuan', fontsize=16)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.text(2,1,r'$\mu=100$', fontsize=15)
plt.axis([-1,6,-2,2])
plt.grid(True)

# 注释箭头
plt.annotate(r'$\mu=100$', xy=(2,1), xytext=(3,1.5), arrowprops=dict(facecolor='black', shrink=0.1,width=2))
plt.show()
