while True:
    try:
        number_1 = int(input("Please enter number1."))
        number_2 = int(input("Please enter number1."))
    except ValueError:
        print("Please enter int number!!!")
    else:
        sum = number_1 + number_2
        print(f"The sum of {number_1} and {number_2} is {sum}.")

    choice = input("Do you want to try again? (yes/no): ").lower()
    if choice != 'yes':
        break