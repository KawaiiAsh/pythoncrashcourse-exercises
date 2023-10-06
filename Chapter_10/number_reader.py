import json

filename = 'number.json'
with open(filename,'r') as file_object:
    numbers = json.load(file_object)

print(numbers)