# 6.1
# personal_informations = {
#     'first_name':'mystery',
#     'last_name':'deer',
#     'age':18,
#     'city':'china',
#     } 

# print(f"{personal_informations['first_name'].title()}")
# print(f"{personal_informations['last_name'].title()}")
# print(f"{personal_informations['age']}")
# print(f"{personal_informations['city'].title()}")

# 6.2
# favorite_numbers = {
#     'ava':3,
#     'james':6,
#     'ethan':8,
#     'emma':9,
#     'lucas':0,
#     }

# print(favorite_numbers)

# 6.3
# glossarys = {
#     'sort':'按字母顺序对列表进行永久排序',
#     'f-format':'把花括号内的变量替换为其值来设置字符串的格式',
#     'rstrip':'确保字符串右端没有空白',
#     'title':'把字符串第一字符变成大写',
#     'lower':'把字符串全部换成小写字符输出',
#     }

# print(f"sort:\n\t{glossarys['sort']}")
# print(f"f-format:\n\t{glossarys['f-format']}")
# print(f"rstrip:\n\t{glossarys['rstrip']}")
# print(f"title:\n\t{glossarys['title']}")
# print(f"lower:\n\t{glossarys['lower']}")

# 6.4
# glossarys = {
#     'sort':'按字母顺序对列表进行永久排序',
#     'f-format':'把花括号内的变量替换为其值来设置字符串的格式',
#     'rstrip':'确保字符串右端没有空白',
#     'title':'把字符串第一字符变成大写',
#     'lower':'把字符串全部换成小写字符输出',
#     'items':'返回一个键值对列表',
#     'keys':'返回一个包含所有键的列表',
#     'values':'返回一个包含所有值的列表',
#     'sorted':'暂时按字母顺序对列表进行排序',
#     'set':'返回字典中所有值并剔重复项后的一个列表',
#     }

# number = 1
# for key,value in glossarys.items():
#     print(f"{number}.{key.title()}:{value}")
#     number += 1

# 6.5
# rivers = {
#     'nile':'egypt',
#     'amszon':'brazil',
#     'yangtze':'china',
#     }

# for river,country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}")
    
# for river in rivers.keys():
#     print(river)

# for country in rivers.values():
#     print(country)

# 6.6
# favorite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil':'python',
#     }

# informants = ['jen','phil','sarah','john','michael']

# for informant in informants:
    # if informant in favorite_languages.keys():
    #     print(f"{informant.title()} thank you for investigate")
    # else:
    #     print(f"{informant.title()} Plesae take our investigate")

# personal_1 = {
#     'first_name':'mystery',
#     'last_name':'deer',
#     'age':18,
#     'city':'china',
#     } 

# personal_2 = {
#     'first_name':'lu',
#     'last_name':'yunqi',
#     'age':10,
#     'city':'japan',
#     } 

# personal_3 = {
#     'first_name':'jia',
#     'last_name':'tingting',
#     'age':28,
#     'city':'america',
#     } 

# peoples = [personal_1,personal_2,personal_3]

# for people in peoples:
#     print(people)

# 6.8
# pet_1 = {'dog':'emily'}
# pet_2 = {'cat':'james'}
# pet_3 = {'bird':'lucas'}

# pets = [pet_1,pet_2,pet_3]

# for pet in pets:
#     print(pet)

# 6.9
# favorite_places = {
#     'emily':['great wall','forbidden'],
#     'lucas':['potala palace','jiuzhaigou valley'],
#     'james':['terracotta army','li river'],
#     }

# for name,places in favorite_places.items():
#     print(f"{name.title()} favotrite places are :")
#     for place in places:
#         print(f"\t{place}")

# 6.10
# favorite_numbers = {
#     'ava':[3,4,5,8],
#     'james':[6,9,1,0],
#     'ethan':[8,2,5,4,7],
#     'emma':[9,2,5,6,3],
#     'lucas':[0,3,6,9,2],
#     }

# for name,numbers in favorite_numbers.items():
#     print(f"{name.title()} favorite number are :")
#     for number in numbers:
#         print(number)

# 6.11
cities = {
    'tokyo':{
        'country':'japan',
        'population':'37.4 million',
        'fact':'The world\'s most populous metropolitan area,with more '
        'Mchelin-starred restaurants than any other city.',
        },

    'paris':{
        'country':'france',
        'population':'11.2 million',
        'fact':'Home to the louvre,the world\'s largest art museum,'
        'where the Mona lisais displayed.',
        },
        
    'cairo':{
        'country':'egypt',
        'population':'22.2 million',
        'fact':'Near the Great Pyramids of Giza,the only surviving'
        'wonderr of the ancient world.',
        },
    }

for cityname,city_info in cities.items():
    print(f"City's name: {cityname.title()}")
    country_info = f"{city_info['population']} {city_info['country']}"
    fact = city_info['fact']

    print(f"\tCountry info: {country_info.title()}")
    print(f"\tFact: {fact.title()}")
