def make_pizza(size,*toppings):
    # """"打印顾客点的所有配料"""
    # print(toppings)

    # """"概述要制作的披萨"""
    # print("\nMaking a pizza with the following toppings:")
    # for topping in toppings:
    #     print(f"-{topping}")

    """"概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')