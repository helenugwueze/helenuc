user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")



friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
           ", i see your favorite language is " +
           favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


for language in set(favorite_languages.values()):
    print(language.title())

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean': 'An expression that evaluates to True or False.',
}
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")


rivers = {
    'congo': 'cental africa',
    'nile': 'egypt',
    'amazon': 'south america'
}    

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for name, country in rivers.items():
    print(name.title())

rivers_data = {
    'congo': 'central africa',
    'nile': 'egypt',
    'amazon': 'south america'
}    
for country in rivers_data.values():
    print(country.title())


poll_responses = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


people_to_poll = ['jen', 'david', 'phil', 'rebecca', 'edward', 'matt']

for person in people_to_poll:
    if person in poll_responses:
        print(f"Thank you, {person.title()}, for responding to our poll!")
    else:
        print(f"Hi {person.title()}, we invite you to take our favorite languages poll!")



