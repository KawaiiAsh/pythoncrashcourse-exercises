class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name + ". " + self.cuisine_type)
    
    def open_restaurant(self):
        print("Restaurant opening...")


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavours):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = flavours

    def show_flavors(self):
        for flavour in self.flavours:
            print(flavour)

flavours = ['chocolate','original','bannana','milk']
my_ice_cream = IceCreamStand('Ice Cream Corner','Ice Cream',flavours)
my_ice_cream.show_flavors()