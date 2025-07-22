"""一个可用于表示用户的类"""

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