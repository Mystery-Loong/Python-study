import plotly.express as px
import pandas as pd

from pathlib import Path
import csv

path = Path('eq_data/world_fires_7_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# 提取经度 纬度 火灾强度
lons, lats, bris = [], [], []
for row in reader:
    lon = float(row[1])
    lat = float(row[0])
    bri = float(row[2])
    lons.append(lon)
    lats.append(lat)
    bris.append(bri)

data = pd.DataFrame(
    data=zip(lons, lats, bris), columns=['经度', '纬度', '火灾强度']
)
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-180, 180],
    range_y=[-60, 80],
    title='全球火灾散点图',
    size='火灾强度',
    size_max=10,
    color='火灾强度',
)

fig.show()