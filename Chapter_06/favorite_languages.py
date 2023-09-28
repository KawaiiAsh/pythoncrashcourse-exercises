favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'] +
      ".")

for name,language in favorite_languages.items():
    print("\nName: " + name + ", Language: " + language)

for name in favorite_languages.keys():
    print("\nName: " + name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name + ". ")
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " + 
              favorite_languages[name].title() + ".")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", Thank you for talking the poll!")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())