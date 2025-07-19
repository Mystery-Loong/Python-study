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
class User:
    """创建用户类包含first_name和last_name"""
    def __init__(self,first_name,last_name):
        """初始化first_name和last_name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """显示登入系统"""
        print(f"\n{self.first_name} {self.last_name} is login now!")

    def greet_user(self):
        """向用户问好"""
        print(f"{self.first_name} {self.last_name} welcome come back!")

one_user = User('Quantum','Panda')
two_user = User('Captain','Churro')

one_user.describe_user()
one_user.greet_user()

two_user.describe_user()
two_user.greet_user()