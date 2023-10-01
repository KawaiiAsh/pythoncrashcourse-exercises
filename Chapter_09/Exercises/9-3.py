class User():
    def __init__(self,first_name,last_name,**informations):
        self.first_name = first_name
        self.last_name = last_name
        self.informations = informations
        for key,value in informations.items():
            setattr(self,key,value)

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        for key, value in self.informations.items():
            print(key + ": " + str(value))

    def greet_user(self):
        print("Hi ! " + self.first_name + ". How are you?")

ash = User('Ash','One',age = 21,gender = 'male')
ash.greet_user()
ash.describe_user()

da = User('Da','Lao',age = 39,gender = 'male')
da.greet_user()
da.describe_user()