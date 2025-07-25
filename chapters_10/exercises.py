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
from pathlib import Path

path = Path('guest_book.txt')
contents = "name:\n"
while True:
    print("Enter 'q' at any time to quit.")
    content = input("Please input you name:")
    if content == 'q':
        break
    else:
        contents += f"\t{content}\n"
path.write_text(contents)
print(contents)