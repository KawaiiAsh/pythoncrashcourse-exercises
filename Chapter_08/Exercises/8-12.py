def add_toppings(*toppings):
    print("Your sandwich include following toppings:")
    for topping in toppings:
        print("- " + topping)

add_toppings('Mushrooms','Extra cheese','Beef')
add_toppings('Hotdog','Extra cheese','Lamb')
add_toppings('Coin','Extra cheese','Fish')  