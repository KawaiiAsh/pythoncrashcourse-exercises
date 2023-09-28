dog = {
    'type':'dog',
    'onwer':'ash',
}

bird = {
    'type':'bird',
    'onwer':'ash',
}

cat = {
    'type':'cat',
    'onwer':'ash',
}

pets = [dog,bird,cat]

for pet in pets:
    print("The type of pet is " + pet['type'].title() + " Onwer is: " + pet['onwer'].title() + ".")