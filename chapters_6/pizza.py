# 存储客户所点披萨的信息
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
    }

# 概述客户点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

