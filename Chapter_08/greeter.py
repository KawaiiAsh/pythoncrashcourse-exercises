def greet_user():
    print("Hello!")

greet_user()

def greet_user(username):
    print("Hello! " + username.title() + ".")

greet_user('ash')


def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("Please tell me your name: ")
    print("Enter 'q' to quit.")
    first_name = input("First name:")

    if first_name == 'q':
        break

    last_name = input("Last_name:")

    if last_name == 'q':
        break
    
    formatted_name = get_formatted_name(first_name,last_name)
    print("Hello, " + formatted_name + "!")