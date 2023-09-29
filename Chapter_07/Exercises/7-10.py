dream_vacation_spots = {}
poll_active = True
while poll_active:
    print("If you could visit one place in the world,where would you go?")
    username = input("What is your username?")
    desired_destination  = input("Where you wanna go?")
    dream_vacation_spots[username] = desired_destination

    repeat = input("You wanna quit? (yes or no)")
    if repeat == 'yes':
        break

for username,desired_destination in dream_vacation_spots.items():
    print(f"{username} wanna go {desired_destination}" + ".")
