while True:
    age = input("May I ask your age?(Enter quit to end program!)")
    if age.lower() == 'quit':
        break
    
    if not age.isdigit():
        print("Please enter a age or 'quit' to exit.")
        continue
    
    age = int(age)
    
    if age >= 0 and age < 3:
        print("The price is free.")
    elif age >= 3 and age <= 12:
        print("The price is $10.")
    else:
        print("The price is $15.")
    
