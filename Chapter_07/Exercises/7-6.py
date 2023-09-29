active = True

while active:
    age = input("May I ask your age? (Enter 'quit' to end the program!) ")

    if age.lower() == 'quit':
        active = False
        break

    if not age.isdigit():
        print("Please enter a valid age or 'quit' to exit.")
        continue
    
    age = int(age)
    
    if age < 3:
        print("The price is free.")
    elif age <= 12:
        print("The price is $10.")
    else:
        print("The price is $15.")
