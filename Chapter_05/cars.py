cars = ['audi','bnw','subaru','toyota']

for car in cars:
    if car == 'bnw':
        print(car.upper())
    else:
        print(car.title())  

car = 'Audi'
print(car.lower() == 'audi')