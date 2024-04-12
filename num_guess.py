# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# Date: 04/09/2024
# NOTE: No ReadMe Using other IDE
# Description: Asks the user to enter an integer that a player will guess. Display whether the guess is too high or too low or displays that the player got it right in x amount of times.

num = int(input("Enter the integer for the player to guess.\n"))

guess = int(input("Enter your guess.\n"))

num_guesses = 1

while True:
    if guess == num:
        if num_guesses == 1:
            print("You guessed it in", num_guesses, "try.")  
        else:
            print("You guessed it in", num_guesses, "tries.")  
        break
    elif guess > num:
        print("Too high - try again:")
    else:    
        print("Too low - try again:")

    guess = int(input())
    num_guesses += 1
        