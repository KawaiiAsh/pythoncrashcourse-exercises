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

class Admin(User):
    def __init__(self, first_name, last_name, privileges ,**informations):
        super().__init__(first_name, last_name, **informations)
        self.privileges = privileges
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{self.first_name}" + " " + privilege)

privileges = ['can add post','can delete post','can ban user']
web_admin = Admin('Ash','One',privileges ,gender = 'Male')
web_admin.show_privileges()


