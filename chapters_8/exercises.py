# 8.1
# def display_message():
#     """"显示本章的主题"""
#     print("The theme of this chapter is function")

# display_message()

# 8.2
# def favorite_book(title):
#     """"显示喜欢的书籍"""
#     print(f"One of my favorite books is {title.title()}.")

# favorite_book('Alice in wonderland')

# 8.3
# def make_shirt(size,words):
#     """"显示T恤尺寸和字样"""
#     print(f"The shirt size is {size},and words is {words.title()}")

# make_shirt(41,"Hello python world!")
# make_shirt(size=41,words='Hello python world!')

# 8.4
# def make_shirt(size,words='I love Python'):
#     """"显示号数和字样"""
#     print(f"Making a {size.title()} shirt,Printed with {words.title()}")

# make_shirt('large size')
# make_shirt('medium size')
# make_shirt('large size','Hello python world')

# 8.5
# def describe_city(city,country='china'):
#     """"显示城市和所属国家名称"""
#     print(f"{city.title()} is in {country.title()}")

# describe_city('beijing')
# describe_city('nanning')
# describe_city('new york','america')

# 8.6
# def city_country(city,country):
#     """"返回规范格式的城市和国家"""
#     messages = {'city':city,'country':country}
#     formatted = f"{messages['city']},{messages['country']}"
#     return formatted

# city_country_message = city_country('beijing','china')
# print(city_country_message)
# city_country_message = city_country('nanning','china')
# print(city_country_message)
# city_country_message = city_country('guiling','china')
# print(city_country_message)

# 8.7
# def make_album(singer,album,songs=None):
#     """"返回包含歌手和专辑的字典"""
#     if songs:
#         person = {'singer':singer,'album':album,'songs':songs}
#     else:
#         person = {'singer':singer,'album':album}
#     return person

# message = make_album('adele','21')
# print(message)
# message = make_album('Michael Jackson','Thriller',16)
# print(message)
# message = make_album('the weeknd','after hours')
# print(message)

# 8.8
# def make_album(singer,album):
#     """"将歌手和专辑存入字典中并返回"""
#     messages = {'singer':singer,'album':album}
#     return messages

# while True:
#     """"输入信息并存入字典中"""
#     Prompt = print("Please enter a singer and album:"
#     "\nenter 'q' at any time to quit")

#     singer = input("singer's name:")
#     if singer == 'q':
#         break

    # album = input("album's name:")
    # if album == 'q':
    #     break

    # person = make_album(singer,album)
    # print(person)

# 8.9
# def show_messages(texts):
#     """"显示列表中每条文本的信息"""
#     for text in texts:
#         print(text)

# list_texts = ['a','b','c','d']
# show_messages(list_texts)

# 8.10
# def send_messages(nonnull_lists,sent_messages):
#     """"显示列表每条信息并移到sent_messages列表中"""
#     while nonnull_lists:
#         list = nonnull_lists.pop()
#         print(f"The list is {list}.")
#         sent_messages.append(list)
    
#     print("The original list are follwing:")
#     for nonnull_list in nonnull_lists:
#         print(nonnull_list)
    
    # print("The sent messages are following:")
    # for sent_message in sent_messages:
    #     print(sent_message)

# nonnull_lists = ['a','b','c','d','e']
# sent_messages = []
# send_messages(nonnull_lists,sent_messages)

# 8.11
# def send_messages(nonnull_lists_1,sent_messages):
#     """"显示列表每条信息并移到sent_messages列表中"""
#     nonnull_lists_1.reverse()
#     while nonnull_lists_1:
#         list = nonnull_lists_1.pop()
#         print(f"The list text is {list}.")
#         sent_messages.append(list)
    
    # print("The original list are follwing:")
    # for nonnull_list in nonnull_lists:
    #     print(nonnull_list)
    
    # print("The sent messages are following:")
    # sent_messages.sort()
#     for sent_message in sent_messages:
#         print(sent_message)

# nonnull_lists = ['a','b','c','d','e']
# sent_messages = []
# send_messages(nonnull_lists[:],sent_messages)

# 8.12
# def making_sandwich(*toppings):
#     """"对客户的三明治食材进行概述"""
#     print("Making sandwich with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping.title()}")

# making_sandwich('mushrooms','extra cheese','pepperoni')
# making_sandwich('mushrooms')
# making_sandwich('extra cheese')

# 8.13
# def build_profile(first,last,**user_info):
#     """"创建一个字典，其中包含我们知道的有关用户的一切"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('mystery','loong',
#                              location='china',
#                              language='python',
#                              foods='ribs')
# print(user_profile)

# 8.14
def build_car_info(maker,model,**car_info):
    """"创建一个字典，返回车辆信息"""
    car_info[maker] = maker
    car_info[model] = model
    return car_info

car_messages = build_car_info('subaru','outback',
                              color='blue',
                              tow_package=True)
print(car_messages)                        
