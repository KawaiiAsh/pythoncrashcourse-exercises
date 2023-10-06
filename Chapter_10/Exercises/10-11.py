import json

favorite_number = input("Please enter your favorite number.")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("File not found.")
else:
    # 打印消息
    print(f"I know your favorite number! It's {favorite_number}.")