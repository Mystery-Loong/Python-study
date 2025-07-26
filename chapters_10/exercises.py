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
from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')
count_the = contents.lower().count('alice')

print(f"The 'alice' appear {count_the} in {path}")