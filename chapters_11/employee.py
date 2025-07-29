# 11.3
class Employee:
    """存储雇员的姓名和年薪"""
    def __init__(self,first_name,last_name,yearly_salary):
        """存储姓名和年薪"""
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_salary = yearly_salary

    def give_raise(self,add=5000):
        """年薪默认增加5000,也可以定制增加"""
        self.yearly_salary += add 

# employee = Employee('Mystery','Loong',10000)
# print(f"The employee {employee.first_name} {employee.last_name}'s yearly salary\
#  is {employee.yearly_salary}")

# employee.give_raise()
# print(f"\nThe employee {employee.first_name} {employee.last_name}'s yearly \
# salary is {employee.yearly_salary} by now!")