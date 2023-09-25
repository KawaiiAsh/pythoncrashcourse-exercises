pizzas = ['beef pizza','chicken pizza','lamb pizza']
friend_pizza = pizzas[:]
pizzas.append("fish pizza")
friend_pizza.append("rabbit pizza")

print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)
print("Friend's favorite pizza are:")
for pizza in friend_pizza:
    print(pizza)
