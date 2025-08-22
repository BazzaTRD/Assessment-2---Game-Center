#Barry

# Add time limit?

# Randomly generate 'n' (input by player) number of numbers from -999 to 999, place them all in a list
# Ask to sort in asc or desc order
# Player will enter the numbers 1 by 1 in the order that they had selected
# The computer will check if the number is the correct one + if the number is in the list. If the selected number is incorrect, the player loses
# The results of the game will be displayed (the correct number for the current guess, how many numbers guessed correct, how many numbers weren't guessed)

import random
import time

def sorting_game(intNumberOf):
    print("\n--- Number Sorting Game ---")
    
    # Setting up the game
    listNumbers = []
    for i in range(1, intNumberOf + 1):
        listNumbers.append(random.randrange(-999, 999))
    print(f"You have chosen to sort '{intNumberOf}' numbers.")
    time.sleep(0.5)
    intNumberOf = len(listNumbers) # Debug
    print(f"\n Your {intNumberOf} numbers are... \n {listNumbers}")
    time.sleep(1)

    #Sorting the list
    stringAscDesc = str(input("\nHow would you like to sort the list? (asc/desc): ")).lower()
    if stringAscDesc == "asc":
        print("You have chosen to sort the list in ASCENDING order!")
        listNumbers.sort()
    elif stringAscDesc == "desc":
        print("You have chosen to sort the list in DESCENDING order!")
        listNumbers.sort(reverse = True)
    time.sleep(.5)
    print("Let the games... BEGIN!!")
    time.sleep(1)

    #Playing the game
    currNumIndex = 0
    listPlayerAns = []
    while currNumIndex < intNumberOf:
        intPlayerAns = int(input(f"\nSorting number {currNumIndex + 1}: "))
        currNumAns = listNumbers[currNumIndex]
        if intPlayerAns != currNumAns:
            print(f"Incorrect! The number was {currNumAns}.")
            return False
        print("Correct!")
        listPlayerAns.append(intPlayerAns)
        print(f"Progress...\n{listPlayerAns}")
        currNumIndex += 1
    return True

play = input("Would you like to play the sorting game? (yes/no): ").lower()
if play == "yes":
    try:
        intNumberOf = int(input("How many numbers would you like to sort?: "))
        sortingReturn = sorting_game(intNumberOf)

        # Return results
        if sortingReturn == True:
            print("\nCongratulations! You have won!")
        else:
            print("\nYou have lost...")
        print("Thanks for playing the Sorting Game!")
    except ValueError as e:
        print(f"Invalid input... Exiting with error code: {e}")
    time.sleep(1)