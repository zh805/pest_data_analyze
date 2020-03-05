import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


plt.style.use('fivethirtyeight')
#绘图设置
fig = plt.figure()
# ax=fig.gca(projection='3d')#三维坐标轴
ax = plt.axes(projection = '3d')
#构造需要显示的值
# X=np.arange(0, 5, step=1)
#X轴的坐标

x = np.array([2, 14, 26, 38, 48])
y = np.array([2, 12, 23])


xx, yy=np.meshgrid(x, y)#网格化坐标
X, Y=xx.ravel(), yy.ravel()#矩阵扁平化
bottom=np.zeros_like(X)#设置柱状图的底端位值
# Z=Z.ravel()#扁平化矩阵
Z = np.array([6,3,2,2,6,4,2,2,4,3,2,11,6,7,6])

width=height=2#每一个柱子的长和宽


ax.bar3d(X, Y, bottom, width, height, Z, shade=True, color='c')

# ax.set_title('各个监测点储粮害虫数量', fontproperties='SimHei', fontsize=12)

#坐标轴设置
# ax.set_xlabel('X')  
# ax.set_ylabel('Y')
ax.set_zlabel('害虫数量(头)', fontproperties='SimHei', fontsize=10)

plt.show()