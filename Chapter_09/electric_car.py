class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.oddmeter = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odemeter(self):
        print("This car has " + str(self.oddmeter)) + " miles on it."

    def update_odemeter(self,mileage):
        if mileage >= self.oddmeter:
            self.oddmeter = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odemeter(self,miles):
        oddmeter += miles

    def fill_gas_tank(self):
        pass

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2016) 
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()