import json


def store_favorite_number(filename):
    try:
        with open(filename,'w',encoding='UTF-8') as file_object:
            favorite_number = int(input("What is your favorite number?"))
            json.dump(favorite_number,file_object)
    except ValueError:
        print("Please input a int number.")     

def read_favorite_number(filename): 
    try:
        with open(filename,'r',encoding='UTF-8') as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        print("File not found!") 
    except json.JSONDecodeError:
        print("Json decode error!")       


filename = 'favorite_number.json'
favorite_number = read_favorite_number(filename)
if favorite_number:
    print(favorite_number)
else:
    favorite_number = read_favorite_number(filename)
    store_favorite_number(filename)
    if favorite_number:
        print(favorite_number)