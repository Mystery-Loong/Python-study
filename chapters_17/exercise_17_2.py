from operator import itemgetter

import requests
import plotly.express as px

# 执行API调用并查看响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # 对于每篇文章，都执行一个API调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
    # 对于每篇文章，都创建一个字典
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
    }
    except KeyError:
        print(f"Missing comments of {response_dict['title']}")

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                          reverse=True)

title_links, comments = [], []
for submission_dict in submission_dicts:
    # print(f"\nTitle: {submission_dict['title']}")        
    # print(f"Discussion link: {submission_dict['hn_link']}")
    # print(f"Comments: {submission_dict['comments']}")
    title = submission_dict['title']
    title_url = submission_dict['hn_link']
    title_link = f"<a href='{title_url}'>{title}</a>"
    title_links.append(title_link)
    comments.append(submission_dict['comments'])

# 可视化
title = "Topstories Comments News on Hacker News"
labels = {'x': 'News titles', 'y': 'Comments'}
fig = px.bar(x=title_links, y=comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.5)

fig.show()