import plotly.express as px

from random import randint

class Die:
    """一个骰子的类"""

    def __init__(self,num_sides):
        """骰子默认为8面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个介于1和骰子面数之间的随机数"""
        number = randint(1,self.num_sides)
        return number
    
# 创建三个D6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3,max_result)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
title = "Results of Rolling Three D6 Dice 100,000 Times"
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# 进一步定制图形
fig.update_layout(xaxis_dtick=1)
fig.show()