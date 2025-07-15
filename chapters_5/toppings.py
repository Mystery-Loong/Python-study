# requested_toppings = ['mushrooms','green peppers','extra cheese']

# if requested_toppings != 'anchovies':
#     print("Hold the anchovies!")

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding peperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry,we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making you pizza!")


# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("fAdding {request_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ['mushroom','olives','green peppers','pepperoni',
                      'pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we are don't have {requested_topping}")
print("\nFinished making your pizza!")