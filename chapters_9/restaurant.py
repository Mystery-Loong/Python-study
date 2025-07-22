"""一个可用于表示餐馆的类"""

class Restaurant:
    """创建一家餐馆"""

    def __init__(self,name,type):
        """初始化属性name和type"""
        self.name = name
        self.type = type
        self.number_served = 1000

    def set_number_served(self,number_served):
        """显示餐馆就餐过的人数"""
        if number_served >= self.number_served:
            self.number_served = number_served
            print(f"The {self.name}-{self.type} restaurant had served {self.number_served} people so far!")
        else:
            print("You can't reduce the served numbers")

    def increment_number_served(self,number):
        """增加指定的人数"""
        print(f"This restaurant serve {number} people every day")