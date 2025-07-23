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
# class User:
#     """创建用户类包含first_name和last_name"""
#     def __init__(self,first_name,last_name):
#         """初始化first_name和last_name"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.attempts = 0

#     def describe_user(self):
#         """显示登入系统"""
#         print(f"\n{self.first_name} {self.last_name} is login now!")

#     def greet_user(self):
#         """向用户问好"""
#         print(f"{self.first_name} {self.last_name} welcome come back!")

#     def increment_login_attempts(self):
#         """登入次数加1"""
#         self.attempts += 1

#     def reset_login_attempts(self):
#         """重置登入次数为0"""
#         self.attempts = 0


# one_user = User('Quantum','Panda')

# one_user.describe_user()
# one_user.greet_user()

# one_user.increment_login_attempts()
# one_user.increment_login_attempts()
# one_user.increment_login_attempts()
# one_user.increment_login_attempts()

# print(f"\n{one_user.first_name} {one_user.last_name} login attempts are {one_user.attempts}")

# one_user.reset_login_attempts()

# print(print(f"\n{one_user.first_name} {one_user.last_name} login attempts reset to {one_user.attempts}"))

# 9.6
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

# class IceCreamStand(Restaurant):
#     """冰淇淋店的特色"""

#     def __init__(self,name,type):
#         """
#         先初始化父类的属性
#         在初始化冰淇淋店的属性
#         """
#         super().__init__(name,type)
#         self.flavors = ['Vanilla','Chocolatr','Strawberry','Mint Chocolate Chip','Cookies and Cream']

#     def show_flavors(self):
#         """显示冰淇淋的口味"""
#         print("The Icecreamstand's flavors is following: ")
#         for flavor in self.flavors:
#             print(f"\t{flavor}")


# my_icecreamstand = IceCreamStand('最好吃','冰淇淋')
# my_icecreamstand.show_flavors()

# 9.7
# class User:
#     """创建用户类包含first_name和last_name"""
#     def __init__(self,first_name,last_name):
#         """初始化first_name和last_name"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.attempts = 0

#     def describe_user(self):
#         """显示登入系统"""
#         print(f"\n{self.first_name} {self.last_name} is login now!")

#     def greet_user(self):
#         """向用户问好"""
#         print(f"{self.first_name} {self.last_name} welcome come back!")

#     def increment_login_attempts(self):
#         """登入次数加1"""
#         self.attempts += 1

#     def reset_login_attempts(self):
#         """重置登入次数为0"""
#         self.attempts = 0

# class Admin(User):
#     """管理员的特权"""
#     def __init__(self,first_name,last_name):
#         """初始化父类属性"""
#         super().__init__(first_name,last_name)
#         self.privileges = ['can add post','can delete post','can ban user']

#     def show_privileges(self):
#         """显示管理员的权限"""
#         print("The Admin's privileges is following: ")
#         for privilege in self.privileges:
#             print(f"\t{privilege}")

# admin = Admin('Mystery','Loong')
# admin.show_privileges()

# 9.8
# class User:
#     """创建用户类包含first_name和last_name"""
#     def __init__(self,first_name,last_name):
#         """初始化first_name和last_name"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.attempts = 0

#     def describe_user(self):
#         """显示登入系统"""
#         print(f"\n{self.first_name} {self.last_name} is login now!")

#     def greet_user(self):
#         """向用户问好"""
#         print(f"{self.first_name} {self.last_name} welcome come back!")

#     def increment_login_attempts(self):
#         """登入次数加1"""
#         self.attempts += 1

#     def reset_login_attempts(self):
#         """重置登入次数为0"""
#         self.attempts = 0

# class Privileges:
#     """特权列表"""
#     def  __init__(self,privileges=[]):
#         """初始化特权属性"""
#         self.privileges = ['can add post','can delete post','can ban user']
    
#     def show_privileges(self):
#         """显示管理员的权限"""
#         print("The Admin's privileges is following: ")
#         for privilege in self.privileges:
#             print(f"\t{privilege}")

# class Admin(User):
#     """管理员的特权"""
#     def __init__(self,first_name,last_name):
#         """初始化父类属性"""
#         super().__init__(first_name,last_name)
#         self.privileges = Privileges()

    

# admin = Admin('Mystery','Loong')
# admin.privileges.show_privileges()

# 9.9
# class Car:
#     """一次模拟汽车的简单尝试"""

#     def __init__(self,make,model,year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """返回格式规范的描述性信息"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """打印一条指出汽车行驶里程的信息"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self,miles):
#         """让里程表读数增加指定的量"""
#         if miles >= self.odometer_reading:
#             self.odometer_reading += miles
#         else:
#             print("You can't roll back an odometer!")

# class Battery:
#     """一次模拟电动汽车电池的简单尝试"""
#     def __init__(self,battery_size=40):
#         """初始化电池的属性"""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """打印一条描述电池容量的消息"""
#         print(f"This car has a {self.battery_size}-kwh battery.")

#     def get_range(self):
#         """打印一条信息，指出电池的续航里程"""
#         if self.battery_size == 40:
#             range = 150
#         else:
#             range = 225
        
#         print(f"This car can go about {range} miles on a full charge.")

#     def upgrade_battery(self):
#         """将电池升级为65"""
#         if self.battery_size != 65:
#             self.battery_size = 65
#             print("\nThis car had upgrade battery size to 65 ")

# class ElectriCar(Car):
#     """电动汽车的独特之处"""            

#     def __init__(self,make,model,year):
#         """
#         初始化父类的属性,再初始化电动汽车特有的属性
#         """
#         super().__init__(make,model,year)
#         self.battery = Battery()


# my_leaf = ElectriCar('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
# my_leaf.battery.upgrade_battery()
# my_leaf.battery.get_range()

# 9.10
# from restaurant import Restaurant

# my_restaurant = Restaurant('最美味','烧烤')
# my_restaurant.set_number_served(5000)

# 9.11
# from admin import Admin

# admin_privileges = Admin('Mystery','Loong')
# admin_privileges.privileges.show_privileges()

# 9.12
# from admin import Admin
# admin_privileges = Admin('Mystery','Loong')
# admin_privileges.privileges.show_privileges()

# 9.13
# """一个骰子的类"""

# from random import randint

# class Die:
#     def __init__(self,sides=6):
#         """初始化属性"""
#         self.sides = sides

#     def roll_die(self):
#         """根据sides范围，返回随机一个数字"""
#         number = randint(1,self.sides)
#         print(number)

# die = Die(20)
# num = 10
# while num:
#     die.roll_die()
#     num -= 1

# 9.14
# from random import choice

# ticket_numbers = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e')

# number = 4
# print("The winning numbers are following: ")
# while number:
#     winning_number = choice(ticket_numbers)
#     number -= 1
#     print(f"\t{winning_number}")

# 9.15
from random import choice

ticket_numbers = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
my_ticket = ['2','5','6','d']
active = True
times = 0

while active:
    num = 4
    winning_numbers = []
    while num:
        number = choice(ticket_numbers)
        winning_numbers.append(number)
        num -= 1

    times += 1
    winning_numbers.sort()
    
    if my_ticket == winning_numbers:
        active = False
    else:
        print(times)
             
print(f"I winning by {times} times")