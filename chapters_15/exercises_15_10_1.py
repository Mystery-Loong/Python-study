import matplotlib.pyplot as plt
import numpy as np

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()

ax.bar(poss_results, frequencies, width=0.8)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()