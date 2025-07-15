# 7.1
# car = input("Please tell me what car you would to hire?")
# print(f"Let me see if I can find you a {car.title()}")

# 7.2
# peoples = input("Please tell me how many people are dining")
# peoples = int(peoples)

# if peoples > 8:
#     print("There are no available tables now.")
# else:
#     print("There are tables available.")

# 7.3
# number = input("Please input a number,"
#     " I'll tell you if it's an integer multiple of 10 ")
# number = int(number)

# if number % 10 == 0:
#     print(f"The number: {number} is integer multiple of 10")
# else:
#     print(f"The number: {number} isn't integer multiple of 10.")

# 7.4
# prompt = "Please inter topping you want:"
# prompt += "\nEnter 'quit' when you are finished."

# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else:
#         print(f"You want the topping is: {topping.title()}")

# 7.5
# prompt = "Please enter you age:"
# prompt += "\nenter 'quit' when you are finished."

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("The movie ticket cost of your is $0")
#     elif 3 <= age < 12:
#         print("The movie ticket cost of your is $10")
#     elif age > 12:
#         print("The movie ticket cost of your is $15")

# 7.8
# 创建一个预定了三个三明治的列表
# 创建一个完成三明治制作的空列表
# sandwich_orders = ['club sandwich','blt sandwich','ham sandwich']
# finished_sandwich = []

# 制作三明治直到做完为止
# 将做好的三明治移到完成三明治列表中
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()

#     print(f"I made your {sandwich.title()}")
#     finished_sandwich.append(sandwich)

# 显示所有已经制作完成的三明治
# print("The follow sandwich have been finished:")
# for sandwich in finished_sandwich:
#     print(sandwich)

# 7.9
# 客户订单列表
# 创建一个已经制作完成的空列表
# sandwich_orders = ['club sandwich','pastrami','blt sandwich','ham sandwich',
#                    'pastrami','pastrami']
# finished_sandwich = []

# 显示五香烟熏牛肉卖完了
# print("The pastrami have been sold out.")

# 删除列表中 pastrami
# while 'pastrami' in sandwich_orders:
#             sandwich_orders.remove('pastrami')

# 制作三明治直到做完为止
# 将做好的三明治移到完成三明治列表中
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()

#     print(f"I made your {sandwich.title()}")
#     finished_sandwich.append(sandwich)

# 显示所有已经制作完成的三明治
# print("The follow sandwich have been finished:")
# for sandwich in finished_sandwich:
#     print(sandwich)

# 7.10
# 创建一个空字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\n What is your name?")
    response = input("If you could visit one place in the world," \
        "where would you go?")
    
    # 将回答存于字典中
    responses[name] = response

    # 看看是否还有人参与调查
    repeat = input("Would you like to let another person response?(yes/no)")
    if repeat == 'no':
        polling_active = False

# 显示调查结果
print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name.title()} like to visit {response.title()}")
    
