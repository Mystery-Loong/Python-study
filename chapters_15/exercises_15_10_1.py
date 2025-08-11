import matplotlib.pyplot as plt

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
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies, width=0.7)

# 设置图题并给坐标轴加上标签
ax.set_title("Results of Rolling a D6 1000 times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

plt.show()