from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# 提取日期和每日降水量
dates, precipitations = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    precipitation = float(row[3])
    dates.append(current_date)
    precipitations.append(precipitation)

# print(precipitations)

# 根据数据绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, color='blue')

# 设置绘图的格式
ax.set_title("Daily Precipitations, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Frecipitations", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()