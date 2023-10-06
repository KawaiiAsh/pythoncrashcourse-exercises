import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename,'r',encoding='UTF-8') as file_object:
            username = json.load(file_object)
    except (FileNotFoundError,json.JSONDecodeError):
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w',encoding='UTF-8') as file_object:
        json.dump(username,file_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()