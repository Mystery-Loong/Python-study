# 9.1 9.2
# class Restaurant:
#     """创建一家餐馆"""

#     def __init__(self,name,type):
#         """初始化属性name和type"""
#         self.name = name
#         self.type = type

#     def describe_restaurant(self):
#         """现实餐馆的name和type"""
#         print(f"\nThe restaurant's name is {self.name}.")
#         print(f"The restaurant type is {self.type}!")

#     def open_restaurant(self):
#         """显示餐馆的营业状态"""
#         print(f"The {self.name}-{self.type} restaurant is opening now!")

# my_restaurant = Restaurant('最美味','烧烤')

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# one_restaurant = Restaurant('Olive Garden','italian')
# two_restaurant = Restaurant('Nobu','Japanese')
# three_restaurant = Restaurant('In-N-Out Burger','Fast Food')

# one_restaurant.describe_restaurant()
# two_restaurant.describe_restaurant()
# three_restaurant.describe_restaurant()

# 9.3
# class User:
#     """创建用户类包含first_name和last_name"""
#     def __init__(self,first_name,last_name):
#         """初始化first_name和last_name"""
#         self.first_name = first_name
#         self.last_name = last_name

#     def describe_user(self):
#         """显示登入系统"""
#         print(f"\n{self.first_name} {self.last_name} is login now!")

#     def greet_user(self):
#         """向用户问好"""
#         print(f"{self.first_name} {self.last_name} welcome come back!")

# one_user = User('Quantum','Panda')
# two_user = User('Captain','Churro')

# one_user.describe_user()
# one_user.greet_user()

# two_user.describe_user()
# two_user.greet_user()

# 9.4
# class Restaurant:
#     """创建一家餐馆"""

#     def __init__(self,name,type):
#         """初始化属性name和type"""
#         self.name = name
#         self.type = type
#         self.number_served = 1000

#     def set_number_served(self,number_served):
#         """显示餐馆就餐过的人数"""
#         if number_served >= self.number_served:
#             self.number_served = number_served
#             print(f"The {self.name}-{self.type} restaurant had served {self.number_served} people so far!")
#         else:
#             print("You can't reduce the served numbers")

#     def increment_number_served(self,number):
#         """增加指定的人数"""
#         print(f"This restaurant serve {number} people every day")

# restaurant = Restaurant('最美味','烧烤')

# restaurant.number_served = 50
# restaurant.set_number_served(2000)
# print(f"The {restaurant.name}-{restaurant.type} restaurant had served {restaurant.number_served} perpeo so far!")
# restaurant.increment_number_served(500)

# 9.5
class User:
    """创建用户类包含first_name和last_name"""
    def __init__(self,first_name,last_name):
        """初始化first_name和last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.attempts = 0

    def describe_user(self):
        """显示登入系统"""
        print(f"\n{self.first_name} {self.last_name} is login now!")

    def greet_user(self):
        """向用户问好"""
        print(f"{self.first_name} {self.last_name} welcome come back!")

    def increment_login_attempts(self):
        """登入次数加1"""
        self.attempts += 1

    def reset_login_attempts(self):
        """重置登入次数为0"""
        self.attempts = 0


one_user = User('Quantum','Panda')

one_user.describe_user()
one_user.greet_user()

one_user.increment_login_attempts()
one_user.increment_login_attempts()
one_user.increment_login_attempts()
one_user.increment_login_attempts()

print(f"\n{one_user.first_name} {one_user.last_name} login attempts are {one_user.attempts}")

one_user.reset_login_attempts()

print(print(f"\n{one_user.first_name} {one_user.last_name} login attempts reset to {one_user.attempts}"))