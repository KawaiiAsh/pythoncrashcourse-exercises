import json

numbers = [2,3,5,7,11,13]

filename = 'number.json'
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)