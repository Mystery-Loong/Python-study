import pytest
from employee import Employee

# def test_give_default_raise():
#     """测试默认值是否是5000"""
#     employee = Employee('Mystery','Loong',10000)
#     employee.give_raise()
#     assert employee.yearly_salary == 15000
    
# def test_give_custom_raise():
#     """测试定制值是否是正确的"""
#     employee = Employee('Mystery','Loong',10000)
#     employee.give_raise(20000)
#     assert employee.yearly_salary == 30000

@pytest.fixture
def employee():
    """一个可供所有测试函数使用的Empolyee 实例"""
    employee = Employee('Mystery','Loong',10000)
    return employee

def test_give_default_raise(employee):
    """测试默认值是否是5000"""
    employee.give_raise()
    assert employee.yearly_salary == 15000

def test_give_custom_raise(employee):
    """测试定制值是否是正确的"""
    employee.give_raise(20000)
    assert employee.yearly_salary == 30000