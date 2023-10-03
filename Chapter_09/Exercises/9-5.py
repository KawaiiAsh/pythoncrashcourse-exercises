class User():
    def __init__(self,first_name,last_name,**informations):
        self.first_name = first_name
        self.last_name = last_name
        self.informations = informations
        self.login_attempts = 0
        for key,value in informations.items():
            setattr(self,key,value)

    def describe_user(self):
        print(self.first_name + " " + self.last_name + " Login attempts: " + str(self.login_attempts))
        for key, value in self.informations.items():
            print(key + ": " + str(value))

    def greet_user(self):
        print("Hi ! " + self.first_name + ". How are you?")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

ash = User('Ash','One',age = 21,gender = 'male')
ash.greet_user()
ash.describe_user()
ash.increment_login_attempts()
ash.describe_user()
ash.reset_login_attempts()
ash.describe_user()
