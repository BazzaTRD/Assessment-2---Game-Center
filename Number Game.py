#Jin

# Number Game description: The game asks the player to guess a radomly 
# generated number between 1 and 100. The player has  


import random 

def number_game():
    print("\n--- Number Guessing Game ---")
    
    target = random.randint(1, 100)
    attempt = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempt += 1
            if guess > target:
                print("Too high!")
            elif guess < target:
                print("Too low!")
            else:
                print("Correct! You guessed the number in " , attempt, "attempts and the number is " , target)
                break   
            if target + 5 > guess > target - 5:
                print("You are very close")             
        except ValueError:
            print("Invalid input. Please enter a number.")
            break

number_game()
