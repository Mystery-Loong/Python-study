motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

# # motorcycles[0] = 'ducati'
# # print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles.insert(0,'ducati')
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)

# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)

# last_owned = motorcycles.pop()
# first_owned = motorcycles.pop(1)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")