age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")

if_else     

age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")
else:
    print("sorry, you are too young to vote.")
    print("please register to vote as soon as you turn 18!")    
age = 12
if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $5.")
else:
    print("your admission cost is $10.")  


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("your admission cost is $" + str(price) + ".")  

Using Multiple elif Blocks

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")              


Omitting the else Block

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("adding mushroom.")
if 'pepperoni' in requested_toppings:
    print("adding peooeroni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")

print("\nFinished making your pizza!")   


alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("you just earned five point from the game")

age = 20

if age >= 18:
    print("You may enter.")

age = 15

if age >= 18:
    print("You may enter.")


alien_colors = ['pink', 'green', 'milk']
if 'pink' in alien_colors:
    print('good one')
else:
    print("oh nooo")

if 'green' in alien_colors:
    print("you just won five point ")
if 'gray' in alien_colors:
    print("you did not win")
else:
    print("you just won ten point")

    age = 19

if age > 18:
    print("You may enter.")
else:
    print("Come back when you are older.")
         
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")

alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")

age = 30

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

favorite_fruits = ['mango', 'banana', 'pineapple']

if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'mango' in favorite_fruits:
    print("You really like mangoes!")

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")

if 'orange' in favorite_fruits:
    print("You really like oranges!")


usernames = ['admin', 'eric', 'sara', 'john', 'maria']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
        usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
current_users = ['admin', 'John', 'Sara', 'eric', 'Maria']
new_users = ['john', 'Peter', 'SARA', 'Linda', 'Tom']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: this username is taken. Please enter a new one.")
    else:
        print(f"{new_user}: this username is available.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")    

             for alien_color in ['green', 'yellow', 'red']:
    if alien_color == 'green':
        print("You earned 5 points!")
    elif alien_color == 'yellow':
        print("You earned 10 points!")
    elif alien_color == 'red':
        print("You earned 15 points!")

age = 30
if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teenager")
elif age < 65:
    print("adult")
else:
    print("elder")

favorite_fruits = ['mango', 'banana', 'pineapple']
for fruit in ['banana', 'mango', 'apple', 'pineapple', 'orange']:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}s!")

usernames = ['admin', 'eric', 'sara', 'john', 'maria']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ['admin', 'John', 'Sara', 'eric', 'Maria']
new_users = ['john', 'Peter', 'SARA', 'Linda', 'Tom']
taken = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in taken:
        print(f"{new_user}: taken, enter a new one.")
    else:
        print(f"{new_user}: available.")

for number in range(1, 10):
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")