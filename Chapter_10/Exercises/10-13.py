import json


def get_new_username(filename):
    username = input("What is your name? ")
    with open(filename, 'w', encoding='UTF-8') as file_object:
        json.dump(username, file_object)
    return username

def get_stored_username(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def greet_user(filename):
    username = get_stored_username(filename)
    if username:
        correct = input(f"Are you {username}? (yes/no) ")
        if correct.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(filename)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you when you come back, {username}!")

filename = 'username.json'
greet_user(filename)
