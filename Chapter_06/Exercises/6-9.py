favorite_place = {
    'Shui':['Chengdu','Xian','Shanghai'],
    'Ash':['US','NY','LA'],
    'Guadra':['Suzhou','Fujian','YelloRiver']
}

for person,places in favorite_place.items():
    print(person.title() + "'s favorite place is:")
    for place in places:
        print(place)
    print()
