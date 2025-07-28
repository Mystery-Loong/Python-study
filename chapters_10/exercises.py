# 10.1
# from pathlib import Path

# path = Path('learning_python.txt')
# contents = path.read_text()

# print(contents)

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# 10.2
# from pathlib import Path

# path = Path('learning_python.txt')
# contents = path.read_text()
# contents = contents.replace('Python','R')

# print(contents)

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# 10.4
# from pathlib import Path

# path = Path('guest.txt')
# contents = input("Please input you name :")

# path.write_text(contents)

# 10.5
# from pathlib import Path

# path = Path('guest_book.txt')
# contents = "name:\n"
# while True:
#     print("Enter 'q' at any time to quit.")
#     content = input("Please input you name:")
#     if content == 'q':
#         break
#     else:
#         contents += f"\t{content}\n"
# path.write_text(contents)
# print(contents)

# 10.6 10.7
# print("Give me two numbers,and I'll divide them.")
# print("Enter 'q' to quit anytime")

# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("You can't divide by text!")
#     else:
#         print(answer)

# 10.8
# from pathlib import Path

# path_cats = Path('cats.txt')
# path_dogs = Path('dogs.txt')

# print(f"Cat's name are: \n{path_cats.read_text()}")
# print(f"Dog's name are: \n{path_dogs.read_text()}")

# 10.9
# from pathlib import Path

# filenames = ['cats.txt','dogss.txt']
# for filename in filenames:
#     path = Path(filename)

#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
        # print(f"Sorry,the file {path} does not exist.")
    #     pass
    # else:
    #     print(f"The {filename} content is: \n{contents}")

# 10.10
# from pathlib import Path

# path = Path('alice.txt')
# contents = path.read_text(encoding='utf-8')
# count_the = contents.lower().count('alice')

# print(f"The 'alice' appear {count_the} in {path}")

# 10.11
# from pathlib import Path
# import json

# favorite_number = input("Pleas enter you favorite number:")

# path = Path('favorite_number.txt')
# contents = json.dumps(favorite_number)
# path.write_text(contents)

# contents = path.read_text()
# number = json.loads(contents)
# print(f"I know your favorite number! It's {number}")

# 10.12
# from pathlib import Path
# import json

# path = Path('favorite_number.json')

# if path.exists():
#     contents = path.read_text()
#     number = json.loads(contents)
#     print(f"I know your favorite number! It's {number}")
# else:
#     contents = input("Please enter you favorite's number: ")
#     number = json.dumps(contents)
#     path.write_text(number)

# 10.13
from pathlib import Path
import json

usermessages = {}
def get_stored_usermessages(path):
    """如果存储了用户名信息，就获取它们"""
    if path.exists():
        contents = path.read_text()
        usermessages = json.loads(contents)
        return usermessages
    else:
        return None

def get_new_usermessages(path):
    """提示用户输入用户名、年龄、性别"""
    username = input("What is your name? ")
    age = input("What is your age? ")
    sex = input("What is your sex? ")
    usermessages['username'] = username
    usermessages['age'] = age
    usermessages['sex'] = sex
    contents = json.dumps(usermessages)
    path.write_text(contents)
    return usermessages

def greet_user():
    """问候用户，并指出其名字、年龄、性别"""
    path = Path('usermessages.json')
    usermessages = get_stored_usermessages(path)
    if usermessages:
        username = usermessages['username']
        answer = input(f"Your user name whether or not is {username.title()}?\
                       yes or no?")
        if answer == 'yes':
            print(f"Welcome back, {username}")
            print(f"Your messages are {usermessages}")
        else:
            usermessages = get_new_usermessages(path)
            username = usermessages['username']
            print(f"We'll remenber you when you come back, {username.title()}")
            print(f"Your messages are {usermessages}")
    else:
        usermessages = get_new_usermessages(path)
        username = usermessages['username']
        print(f"We'll remenber you when you come back, {username.title()}")
        print(f"Your messages are {usermessages}")
greet_user()