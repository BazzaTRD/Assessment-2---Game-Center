import subprocess

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
            subprocess.run(["python", "Number Game.py"])
        elif choice == "2":
            subprocess.run(["python", "Rock Paper Scissors.py"])
        elif choice == "3":
            subprocess.run(["python", "Sorting Game.py"])
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