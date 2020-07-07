"""A number-guessing game."""

import random


round = 1 # tracks number of games
best_score = 0

name = input("Howdy, what's your name? \n(Type your name.) ")

print(f"{name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.")

while True:

    number = random.randint(1, 101) # target number
    count = 0 # tracks number of guesses

    guess = input("Your guess? ")
    count += 1 # count first guess

    while guess != number:

        try:
            guess = int(guess) # convert input to an integer

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

        except:
            print("Nope! You must enter a number between 1 and 100.")
            guess = input("Your guess? ")

    if count > best_score:
        best_score = count

    print(f"Well done, {name}! You guessed the correct number!")
    play_again = input("Would you like to play again? Type 'y' for yes and 'n' for no. ")

    if play_again == 'y':
        round += 1
        continue
    else:
        break

print(f"Thanks for playing! Your best score was {best_score} tries!")
