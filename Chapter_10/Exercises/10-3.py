filename = 'guest.txt'
active = ''
with open(filename,'a') as file_object:
    while True:
        guest_name = input("Please enter a guest's name.(enter quit to end the program)")
        if guest_name.title() == 'Quit':
            break
        else:
            file_object.write(guest_name + "\n")
            print("Thank you! " + guest_name.title() + " has been added.")
