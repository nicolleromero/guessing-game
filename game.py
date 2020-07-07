"""A number-guessing game."""

import random

number = random.randint(1, 101) #target number
count = 0 # tracks number of guesses

name = input("Howdy, what's your name? \n(type in your name) ")

print(f"{name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.")

guess = input("Your guess? ")

while guess.isdigit() != True:
    print("Nope! You must enter a number between 1 and 100.")
    guess = input("Your guess? ")

guess = int(guess)

while guess > 100 or guess < 1:
    print("Nope! You must enter a number between 1 and 100.")
    guess = int(input("Your guess? "))

count += 1

while guess != number:

    while guess > 100 or guess < 1:
        print("Nope! You must enter a number between 1 and 100.")
        guess = int(input("Your guess? "))

    if guess < number:
        print("Your guess is too low, try again.")
        guess = int(input("Your guess? "))
        count += 1

    if guess > number:
        print("Your guess is too high, try again.")
        guess = int(input("Your guess? "))
        count += 1

print(f"Well done, {name}! You found my number in {count} tries!")
