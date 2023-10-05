filename = 'programming_reasons.txt'
programming_reasons = {}

while True:
    # 询问并获取用户名
    username = input("Please enter your name (or 'quit' to exit): ")
    
    if username.lower() == 'quit':
        break
    
    reason = input(f"Hello, {username.title()}! Why do you like programming? ")
    
    programming_reasons[username] = reason

    # 将原因写入文件
    with open(filename, 'a') as file:
        file.write(f"{username}: {reason}\n")
        print(f"Thanks, {username.title()}! Your reason has been added to {filename}.")

for name, reason in programming_reasons.items():
    print(f"{name.title()}: {reason}")
