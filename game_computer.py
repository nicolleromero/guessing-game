"""A number-guessing game."""

import random

range = [1, 101] # target number
count = 0 # tracks number of guesses

name = input("Hiya, what's your name? \n(Type your name.) ")

print(f"{name}, think of a number between {range[0]} and {range[1]}.")

number = int(input("What is the number? "))

print("The computer will now attempt to guess your number.")
guess = int((range[1] + range[0]) // 2)

while guess != number:

    if guess > number:
        print(f"{guess} is too high")
        range[1] = guess
        guess = int((range[1] + range[0]) // 2)
        count += 1

    if guess < number:
        print(f"{guess} is too low")
        range[0] = guess
        guess = int((range[1] + range[0]) // 2)
        count += 1


print(f"{number} is your number! The computer guessed your number in {count} tries!")
