"""一个可用于表示管理员特权的类"""

from user import User

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

class Privileges:
    """特权列表"""
    def  __init__(self,privileges=[]):
        """初始化特权属性"""
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        """显示管理员的权限"""
        print("The Admin's privileges is following: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    """管理员的特权"""
    def __init__(self,first_name,last_name):
        """初始化父类属性"""
        super().__init__(first_name,last_name)
        self.privileges = Privileges()