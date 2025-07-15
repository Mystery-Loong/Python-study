# 5.1
# car = 'subaru'
# print("Is car == 'suaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict false.")
# print(car == 'audi')

# food = 'seafood'
# print("\nIs food == 'seafood'? I predict True.")
# print(food == 'seafood')

# print("\nIs food == 'ice cream'? I predict False.")
# print(food == 'ice cream')

# age = 20
# print("\nIs age == 19? I predict False.")
# print(age == 19)

# print("\nIs age == 20? I predict True.")
# print(age == 20)

# topping = 'onions'
# print("\nIs topping == 'mushroom'? I predict False.")
# print(topping == 'mushroom')

# print("\nIs topping == 'onions'? I predict True.")
# print(topping == 'onions')

# number = 99
# print("\nIs number == 66? I predict False.")
# print(number == 66)

# print("\nIs number == 99?I predict True.")
# print(number == 99)

# 5.2
# string = 'Hello python world'
# print("Is string == 'Hello'?")
# print(string == 'Hello')

# print("\nIs string == 'Hello python world'?")
# print(string == 'Hello python world')

# print("\nIs string.lower() == 'hello python world'? ")
# print( string.lower() == 'hello python world')

# print("\nIs string.lower() == 'Hello python world'? ")
# print( string.lower() == 'Hello python world')

# number = 40
# print("Is number >= 45 ? ")
# print(number >= 45)

# print("Is number <= 40?")
# print(number <= 40)

# print("Is number > 30 ? and number < 35 ?")
# print(number > 30 and number < 35)

# print("Is number != 50? or number < 60?")
# print(number != 50 or number < 60)

# numbers = [1,2,3,4,5,6,7,8]
# number = 10
# print("Is number in numbers?")
# print(number in numbers)

# print("\nIs number in numbers[:3]")
# print(number in numbers[:3])

# print("Is number not in numbers?")
# print(number not in numbers)

# print("Is number not in numbers?")
# print(number not in numbers)

# 5.3
# alien_color = 'red'
# if alien_color == 'green':
#     print("Players receive 5 points")

# 5.4
# alien_color = 'yellow'
# if alien_color == 'green':
#     print("Players eliminate an alien, Get 5 points")
# else:
#     print("Players get 10 points")

# 5.5
# alien_color = 'red'
# if alien_color == 'green':
#     print("Players get 5 points.")
# elif alien_color == 'yellow':
#     print("Players get 10 points.")
# else:
#     print("Players get 15 points.")

# 5.6
# age = 43
# if age < 2:
#     print("This person is a baby.")
# elif 2 <= age < 4:
#     print("This person is a child.")
# elif 4 <= age <13:
#     print("This person is a children")
# elif 13 <= age < 18:
#     print("This person is a teenagers")
# elif 18 <= age < 65:
#     print("This person is a middle-age and young person.")
# else:
#     print("This person is an elderly person.")

# 5.7
# favorite_fruits = ['apple','banana','orange','strawberry']
# if 'apple' in favorite_fruits:
#     print("You really like apple!") 
# if 'banana' in favorite_fruits:
#     print("You really like banana!")
# if 'orange' in favorite_fruits:
#     print("You really like orange!")
# if 'grape' in favorite_fruits:
#     print("You really like grape!")
# if 'watermelon' in favorite_fruits:
#     print("You really like watermelon!")

# 5.8
# users = ['neo','luna','vex','zara','admin']
# for user in users:
#     if user == 'admin':
#         print(f"\nHello {user},would you like to see a status report?")
#     else:
#         print(f"Hello {user},thank you for logging in again.")

# 5.9
# users = []
# if users:
#     for user in users:
#         if user == 'admin':
#             print(f"\nHello {user},would you like to see a status report?")
#         else:
#             print(f"Hello {user},thank you for logging in again.")
# print("We need to find some  users.")

# 5.10
# current_users = ['neo','LUNA','vex','zara','admin']
# new_users = ['NEO','luna','odin','rex','jolt']

# current_users_lowers = [current_users_lower.lower() for current_users_lower 
#                         in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lowers:
#         print(f"{new_user} already used,Please input a another name.")
    # else:
    #     print(f"{new_user} isn't used.")

# 5.11
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")