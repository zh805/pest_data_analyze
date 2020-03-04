from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib
from scipy import interpolate
import matplotlib.pyplot as plt 
import numpy as np 


# fig, ax = plt.subplots()
# fig = plt.figure()
# ax = plt.axes()

#指定图形的字体
font = {'family' : 'SimHei',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 10,
        }

# 设置想(x,y)坐标点
x = np.linspace(1, 49, 10)
y = np.linspace(1, 24, 6)
X, Y = np.meshgrid(x, y)

# 10*6 个设备点 
# Z值表示虫口密度
Z = np.array(
    [[6,3,2,2,6,2,2,2,9,2],
    [3,2,5,6,7,9,5,2,2,2],
    [2,2,2,9,13,10,2,2,2,2],
    [4,2,2,1,2,2,2,2,2,7],
    [2,5,2,1,2,2,5,2,2,2],
    [2,2,2,1,7,2,2,2,8,2]])

# 二维插值
f = interpolate.interp2d(x, y, Z, kind='cubic')

x_new = np.linspace(0, 50, 1000)
y_new = np.linspace(0, 25, 600)

# ax = ax.contourf(x_new, y_new, f(x_new, y_new), levels=800, cmap='coolwarm') #colormap: rainbow jet coolwarm bwr

#设定每个图的colormap和colorbar所表示范围是一样的，即归一化
norm = matplotlib.colors.Normalize(vmin=0, vmax=20)

gci = plt.imshow(f(x_new, y_new), extent=(0,50,0,25), cmap='YlOrRd',norm=norm)

ax = plt.gca()

# 设置x轴 y轴 刻度
ax.set_xticks(np.linspace(0,50,11))
ax.set_xticklabels( ('0', '5', '10', '15', '20',  '25',  '30',  '35', '40', '45', '50'))
ax.set_yticks(np.linspace(0,25,6))
ax.set_yticklabels( ('0', '5', '10', '15', '20','25'))

cbar = plt.colorbar(gci)
# cbar.set_label('虫口密度',fontdict=font)
# cbar.set_label('虫口密度',fontproperties='Kaiti')
cbar.set_ticks(np.linspace(0,20,6))
cbar.set_ticklabels( ('0', '4', '8', '12', '16', '20'))

#设置label
# ax.set_ylabel('Land Surface Emissivity',fontdict=font)
# ax.set_xlabel('Land Surface Temperature(K)',fontdict=font) #陆地地表温度LST
#设置title
# ax.set_title('虫口密度热力图', fontproperties='SimHei', fontsize=12)

plt.show()