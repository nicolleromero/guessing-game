"""A number-guessing game."""

import random


round = 1 # tracks number of games
max_tries = 10
best_score = max_tries + 1 # least number of tries in a game
min_range = ""
max_range = ""

name = input("Hiya, what's your name? \n(Type your name.) ")


while True:

    count = 0 # tracks number of guesses

    while type(min_range) != int or type(max_range) != int:
        min_range = input("What would you like the beginning of the range to be? ")
        max_range = input("What would you like the end of the range to be? ")

        try:
            min_range = int(min_range)
            max_range = int(max_range)

        except:
            print("You must enter a number for both the beginning and the end of the range.")
            continue

    number = random.randint(min_range, max_range) # target number
    print(f"{name}, I'm thinking of a number between {min_range} and {max_range}.\nTry to guess my number in fewer than {max_tries} guesses.")

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

            if count > max_tries:
                print(f"Sorry, you exceeded the max number of tries (max is {max_tries}).")
                break

        except:
            print("Nope! You must enter a number between 1 and 100.")
            guess = input("Your guess? ")

    if count < best_score:
        best_score = count

    if guess == number and count > 1:
        print(f"Well done, {name}! You guessed the correct number in {count} tries!")

    if guess == number and count == 1:
        print(f"Well done, {name}! You guessed the correct number in one try!")
    
    play_again = input("Would you like to play again? Type 'y' for yes and 'n' for no. ")

    if play_again == 'y':
        round += 1
        continue
    else:
        if best_score > 1:
            print(f"Thanks for playing! Your best score was {best_score} tries!")

        if best_score == 1:
            print(f"Thanks for playing! Your best score was one try!")

    break

