#Jin
import random

def number_game():
    print("\n--- Number Guessing Game ---")
    target = random.randint(1, 100)
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > target:
            print("Too high!")
        elif guess < target:
            print("Too low!")
        else:
            print("Correct! You guessed the number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

number_game()