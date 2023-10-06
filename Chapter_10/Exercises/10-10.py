import json

filename = 'favorite_number.json'

try:
    with open(filename,'w',encoding='UTF-8') as file_object:
        favorite_number = int(input("What is your favorite number?"))
        json.dump(favorite_number,file_object)
except ValueError:
    print("Please enter a int number.")

try:
    with open(filename,'r',encoding='UTF-8') as file_object:
        favorite_number = json.load(file_object)
except (FileNotFoundError,json.JSONDecodeError):
    print("File not found.")
else:        
    print("I know your favorite number! It's " + str(favorite_number) + ".")