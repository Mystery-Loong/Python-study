# favorite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil':'python',
#     }

# langeage = favorite_langeages['sarah'].title()
# print(f"Sarah's favorite langeage is {langeage}")

# for name in favorite_languages.keys():
    # print(f"{name.title()}'s favorite language is {language.title()}")
    # print(name.title())

# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}")

# if 'erin' not in favorite_languages.keys():
#     print("Erin,please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

favorite_languages = {
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
    }

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t {language.title()}")