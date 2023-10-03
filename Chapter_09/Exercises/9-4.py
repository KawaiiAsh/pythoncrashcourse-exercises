class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + ". " + self.cuisine_type)
        print("There has " + str(self.number_served) + " person rate......")

    def open_restaurant(self):
        print("Restaurant opening...")

    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self,estimated_number):
        self.number_served += estimated_number
    
my_restaurant = Restaurant('Happy Pizza','Pizza')

my_restaurant.open_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served(50)
my_restaurant.describe_restaurant()
