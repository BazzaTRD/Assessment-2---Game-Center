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


def rock_paper_scissors():
    print("\n--- Rock Paper Scissors ---")
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice.")
        return
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")


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


def main():
    print("🎮 Welcome to the Game Center! 🎮")
    while True:
        print("\nChoose a game:")
        print("1. Number Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Number Sorting Game")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            number_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            sorting_game()
        elif choice == "4":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

        again = input("\nWould you like to play another game? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing. Goodbye!")
            break

    main()
