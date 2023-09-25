car = 'toyota'
print(car.title() == 'Toyota')# True
print(car.lower() == 'toyota')# True

number1 = 10
number2 = 20

print(number1 < number2)# True
print(number1 <= number2)# True
print(number1 == number2)# False
print(number1 >= number2)# False
print(number1 > number2)# False

print(number1 == 10 and number2 == 20)#True
print(number1 == 10 or number2 == 21)#True

foods = ['pizza','apple','beef']
print('lamb' in foods)# False
print('lamb' not in foods)# True