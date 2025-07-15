# 4.1
# pizzas = ['durian pizza','fruit pizza','ham pizza']
# for pizza in pizzas:
#     # print(pizza)
#     print(f"I like {pizza.title()}")
# print("I really love pizza!")

# 4.2
# dogs = ['corgi','shiba lnu','golden retriever']
# for dog in dogs:
#     # print(dog)
#     print(f"{dog.title()} would make a great pet.")
# print("Any of these animals would make a great prt!")

# 4.3
# for value in range(1,21):
#     print(value)

# 4.4
# for value in range(1,1000000):
#     print(value)

# 4.5
# values = list(range(1,1000_001))
# print(values)
# print(f"min number:{min(values)},\nMAX number:{max(values)}")
# sum = sum(values)
# print(sum)

# 4.6
# odd_numbers = list(range(1,20,2))
# print(odd_numbers)

# 4.7
# multiple_3 = list(range(3,30,3))
# print(multiple_3)

# 4.8
# cubes = []
# for cube in range(1,11):
#     cube = cube**3
#     cubes.append(cube)
#     print(cube)
# print(cubes)

# 4.9
# cubes = [value**3 for value in range(1,11)]
# print(cubes)

# 4.10
# foods = ['pizza','falafel','carrot cake','cannoli','ice cream']

# print("The first three foods in the list are:")
# print(foods[:3])

# print("\nThree foods from the middle of the list are:")
# print(foods[1:4])

# print("\nThe last three foods in the list are:")
# print(foods[-3:])

# 4.11
# my_pizzas = ['durian pizza','fruit pizza','ham pizza']
# friend_pizzas = my_pizzas[:]

# my_pizzas.append('hawaiian pizza')
# friend_pizzas.append('seafood pizza')

# print("My favorite pizzas are:")
# print(my_pizzas)
# for pizza in my_pizzas:
#     print(pizza)

# print("\nMy friend's favorite pizzas are:")
# print(friend_pizzas)
# for pizza in friend_pizzas:
#     print(pizza)

# 4.13
foods = ('salads','ham','salmon','chicken','fish','sushi')
for food in foods:
    print(food)

# foods[0] = 'cake'                          
print('\n')
foods = ('cake','ham','ice cream','chicken','fish','sushi')
for food in foods:
    print(food)