participants_with_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

invited_people_list = ['jen', 'ash', 'sarah']

for person in invited_people_list:
    if person in participants_with_languages:
        print(person.title() + ", thank you for taking the poll!")
    else:
        print(person.title() + ", please take the poll!")
