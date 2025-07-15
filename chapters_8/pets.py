def describe_pet(pet_name,animal_type='dog'):
    """"显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='harry',animal_type='hamster')
# describe_pet('dog','willie')

# 一条名为 Willie 的小狗
describe_pet('willie')
describe_pet(pet_name='Willie')

# 一只名为Harry的仓鼠
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
