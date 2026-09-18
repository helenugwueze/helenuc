# magicians = ['alice', 'david', 'carolina']
#  for magician in magicians:
#     print(magician)
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
#     print("Thank you, everyone. That was a great magic show!")


# foods = ["rice","beans","bread"]
# for food in foods:
#     print(food)
#     print(", i like to eat " + food.title())
#     print("i can't wait to eat, " + food.title() + ".\n")
#     print("i like it because sweet and gives energy")

# animals = ['fish','goat','dog','sheep']
# for animal in animals:
#     print(animal)
#     print(animal.title() + ", will make a great pet")
#     print("you are an amazing animal " + animal.title() + ".\n")

# making numerical lists

# for value in range(1,5):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
#     squares.append(value**2)
# print(squares)

# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# list comprehensions

# squares = [value**2 for value in range(1,11)]
# print(squares)


# for value in range(1,20):
#     print(value)

# numbers = list(range(1,1000001))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for odd_number in range(1,21,2):
#     print(odd_number)

# multiple_of_three = list(range(3,30,3))
# for number in multiple_of_three:
#     print(number)

# cubes = []
# for number in range(1, 11):
#     cube = number ** 3
#     cubes.append(cube)
# for cube in cubes:
#     print(cube)
 
# cubes = [value**3 for value in range(1,11)]
# print(cubes)

# slicing in a list

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[-3:])

# looping through a slice
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# foods = ['beans','rice','bread','yam']
# print("these are the first three item")
# print(foods[0:3])

# print("these are the three item on middle side")
# print(foods[1:3])

# print("these are the three item in the last")
# print(foods[2:]

# my_pizzas = ['margherita', 'pepperoni', 'bbq chicken']
# friend_pizzas = my_pizzas[:]

# my_pizzas.append('mushroom')
# friend_pizzas.append('hawaiian')

# print("My favorite pizzas are:")
# for pizza in my_pizzas:
#     print(pizza)

# print("\nMy friend’s favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza)

# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)
# print(dimensions[0])
# print(dimensions[1])

# # print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)


# menu = ("pizza", "falafel", "carrot cake", "cannoli", "ice cream")

# print("Original menu:")
# for food in menu:
#     print(f"- {food}")

# print("\n")

# menu = ("burger", "tacos", "carrot cake", "cannoli", "ice cream")

# print("Revised menu:")
# for food in menu:
#     print(f"- {food}")

   

my_pizzas = ["pepperoni", "margherita", "bbq chicken"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("supreme")
friend_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")








