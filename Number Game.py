#Jin

# Number Guessing Game Descreption: The game asks the player to guess a randomly generated number between 1 and 100. 
# Hint will be given either too low or too high for next guess. 
# The player has as many guesses till they guessed it right.
# Number of attempts will be counted.
# Hint will be also given when the guess is within -5, +5 range.


import random                                  # Generate random number


def number_game():                             # define number_game function
    print("\n--- Number Guessing Game ---")    # show name of the game
    
    target = random.randint(1, 100)            # limit the random number to be between 1 and 100 
    attempt = 0                                # start counting for number of attempts

    while True:                                # while loop when True
        try:                                   # try and except block is to ensure errors can be handled gracefully            
            guess = int(input("Guess a number between 1 and 100: "))      # ask the player to guess a number between 1 and 100
            attempt += 1                                                  # each guess will be accounted as one attempt
            if guess > target:                                            # if guessed number is greater than random number
                print("Too high!")                                        # print too high
            elif guess < target:                                          # if guessed number is less than random number
                print("Too low!")                                         # print too low
            else:                                                         # otherwise
                print("Correct! You guessed the number in " , attempt, "attempts and the number is " , target) # print Correct! 
                                                         # You guessed the number with number of attempts and the random number
                break                                    # end the loop if guessed right
            if guess - 5 < target < guess + 5:           # additional condition if the guess is close to target by -5 or +5
                print("You are very close.")             # print You are very close.
        except ValueError:                               # try/except block to handle possible errors
            print("Invalid input. Please enter a number only and try again. ")   # print Invalid input. Remind to enter number only
                                                                                 # and try again.
            break                                             # when error occurred, end the game.

number_game()                                                 # call the function
