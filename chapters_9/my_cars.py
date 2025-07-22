# from car import Car,ElectricCar
# import car

from car import Car
# from electric_car import ElectricCar as EC
import electric_car as ec

my_mustang = Car('ford','mustang',2025)
print(my_mustang.get_descriptive_name())

my_leaf = ec.ElectricCar('nissan','leaf',2025)
print(my_leaf.get_descriptive_name())