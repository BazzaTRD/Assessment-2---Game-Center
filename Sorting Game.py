#Barry

# Randomly generate 'n' (input by player) number of numbers from -999 to 999, place them all in a list
# Ask to sort in asc or desc order
# Player will enter the numbers 1 by 1 in the order that they had selected
# The computer will check if the number is the correct one + if the number is in the list. If the selected number is incorrect, the player loses
# The results of the game will be displayed (the correct number for the current guess, how many numbers guessed correct)

# Basic modules
import random
import time
# Used to write to the file
import sys
from Game_Center import write_result

def sorting_game(intNumberOf):
    print("\n--- Number Sorting Game ---")
    
    # Setting up the game
    listNumbers = []
    for i in range(0, intNumberOf):
        listNumbers.append(random.randrange(-999, 999))
    print(f"You have chosen to sort '{intNumberOf}' numbers.")
    time.sleep(0.5)
    intNumberOf = len(listNumbers) # Debug
    print(f"\nYour {intNumberOf} numbers are... \n {listNumbers}")
    time.sleep(1)

    #Sorting the list
    stringAscDesc = str(input("\nHow would you like to sort the list? (asc/desc): ")).lower()
    if stringAscDesc == "asc":
        print("You have chosen to sort the list in ASCENDING order!")
        listNumbers.sort()
    elif stringAscDesc == "desc":
        print("You have chosen to sort the list in DESCENDING order!")
        listNumbers.sort(reverse = True)
    else:
        print("You have exited the game.")
        return
    time.sleep(.5)
    print("Let the games... BEGIN!!")
    time.sleep(1)

    #Playing the game
    currNumIndex = 0
    listPlayerAns = []
    while currNumIndex < intNumberOf:
        try:
            intPlayerAns = int(input(f"\nSorting number {currNumIndex + 1}: "))
            currNumAns = listNumbers[currNumIndex]
            if intPlayerAns != currNumAns:
                print(f"Incorrect! The number was {currNumAns}.")
                print(f"You guessed {currNumIndex} out of {intNumberOf} numbers correctly.")
                return False
            print("Correct!")
            listPlayerAns.append(intPlayerAns)
            print(f"Progress...\n{listPlayerAns}")
            currNumIndex += 1
        except ValueError:
            print("Please enter a number")
    return True

play = input("Would you like to play the sorting game? (yes/no): ").lower()
if play == "yes":
    try:
        intNumberOf = int(input("How many numbers would you like to sort?: "))
        sortingReturn = sorting_game(intNumberOf)

        # Return results
        if sortingReturn == True:
            print("\nCongratulations! You have won!")
        elif sortingReturn == False:
            print("\nYou have lost...")
        #Write result to file
        write_result(3, sortingReturn, sys.argv[1])
    except ValueError as e:
        print(f"Invalid input... Reason: {e}")
    except NameError as e:
        print(e)
    finally:
        print("Thanks for playing the Sorting Game!")
    time.sleep(1)
