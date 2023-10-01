class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie',5)
your_dog = Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("Your dog's name is " + your_dog.name + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()