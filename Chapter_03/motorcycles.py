motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
# Update element
motorcycles[0] = 'ducati'
print(motorcycles)
# Append element
motorcycles.append('ducati')
print(motorcycles)

# Using Append() create list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Insert element
motorcycles.insert(0,'ducati')
print(motorcycles)

# Del element
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)

# Pop element
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)
first_owned = motorcycles.pop(0)
print(first_owned)
print(motorcycles)

# Remove element
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive.title()+" is too expensive for me")
