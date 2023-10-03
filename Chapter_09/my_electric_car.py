from car import Electric_car

my_tesla = Electric_car('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()