toppings = []

while True:
    topping = input("Please enter your desired pizza toppings (Enter 'quit' to end): ")
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(topping + " Added!")

if len(toppings) > 0:
    print("Your toppings:")
    for topping in toppings:
        print(topping)
else:
    print("No topping")