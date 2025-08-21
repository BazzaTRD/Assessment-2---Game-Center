#Barry

# Randomly generate 'n' (input by player) number of numbers from -999 to 999, place them all in a list
# Ask to sort in asc or desc order
# Player will enter the numbers 1 by 1 in the order that they had selected
# The computer will check if the number is the correct one. If the selected number is incorrect, the player loses
# The results of the game will be displayed (the correct number for the current guess, how many numbers guessed correct, how many numbers weren't guessed)

def sorting_game():
    print("\n--- Number Sorting Game ---")
    numbers = []
    while len(numbers) < 5:
        try:
            num = int(input(f"Enter number {len(numbers) + 1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    order = input("Sort in ascending or descending order? (asc/desc): ").lower()
    if order == "asc":
        numbers.sort()
        print("Sorted in ascending order:", numbers)
    elif order == "desc":
        numbers.sort(reverse=True)
        print("Sorted in descending order:", numbers)
    else:
        print("Invalid option. Displaying original list:", numbers)

play = input("Would you like to play the sorting game? (yes/no): ").lower()
if play == "yes":
    sorting_game()