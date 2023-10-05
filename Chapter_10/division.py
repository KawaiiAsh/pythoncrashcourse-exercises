try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divine by zero!")

print("Give me two numbers. and I'll divine them.")
print("Enter 'q' to quit.")

while True:
    first_number = int(input("\nFirst number:"))
    if first_number == 'q':
        break
    second_number = int(input("\nFirst number:"))
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divine by 0.")
    else:
        print(answer)
