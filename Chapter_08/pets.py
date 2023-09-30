def describe_pet(animal_type='dog',pet_name='willie'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet()