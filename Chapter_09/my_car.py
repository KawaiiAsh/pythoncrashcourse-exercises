from car import Car
from electric_car import Electric_car

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = Electric_car('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())