import matplotlib.pyplot as plt 

labels = 'gudu', 'chini', 'hah', 'jdfj'
sizes = [15, 45, 20, 30]
explods = (0,0.1,0,0)

plt.pie(sizes, explode=explods, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
