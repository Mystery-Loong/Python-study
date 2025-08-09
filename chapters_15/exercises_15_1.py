import matplotlib.pyplot as plt

x_cubes = range(1,6)
y_cubes = [x**3 for x in x_cubes]

x_cubes_2 = range(1,5001)
y_cubes_2 = [x**3 for x in x_cubes_2]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_cubes,y_cubes,c=y_cubes,cmap=plt.cm.Blues,s=100)

fig, ax2 = plt.subplots()
ax2.scatter(x_cubes_2,y_cubes_2,c=y_cubes_2,cmap=plt.cm.Blues,s=10)

# 设置图题并给坐标轴加上标签
ax.set_title("Cube Number",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of Value",fontsize=14)

ax2.set_title("Cube Number",fontsize=24)
ax2.set_xlabel("Value",fontsize=14)
ax2.set_ylabel("Cube of Value",fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)
ax2.tick_params(labelsize=14)

# 设置每个坐标轴的取值范围
ax2.axis([0,5500,0,130_000_000_000])
# ax2.ticklabel_format(style='plain')

plt.show()
