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
    def __init__(self, first_name, last_name ,privileges,**informations):
        super().__init__(first_name, last_name, **informations)
        self.privileges = privileges

class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self,admin_instance):
        for privilege in self.privileges:
            print(admin_instance + " " + privilege)

admin_privileges = Privileges()

web_admin = Admin('Ash','One',admin_privileges,gender = 'Male')
web_admin.privileges.show_privileges(web_admin.first_name)
