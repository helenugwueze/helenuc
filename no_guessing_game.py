import random

secret_number = random.randint(1, 50)

print("I'm thinking of a number between 1 and 50.")

while True:
    guess_text = input("Enter your guess: ")
    guess = int(guess_text)

    if guess == secret_number:
        print("Correct! You got it.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")