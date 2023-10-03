class Battery():
    def __init__(self,bettery_size = 60):
        self.battery_size = bettery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 60:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh!")
        else:
            print("The battery is already 85 kWh.") 

class ElectricCar():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_tesla = ElectricCar('tesla', 'model s', 2022)

print(my_tesla.describe_car())
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()