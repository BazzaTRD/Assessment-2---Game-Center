import os
import subprocess

def read_result(user_file, list_template):
    #place values in a list
    #print out results
    list_file_content = []

    print(f"\nYour current results are:")
    try:
        #ensure the contents of the file are as expected
        with open(user_file) as file:
            for i, content in enumerate(file.readlines()):
                list_file_content.append(content)
                match i:
                    case 0 | 3 | 6:
                        if content.strip() != list_template[i]:
                            print(f"'{content.strip()}' Does not exist... Expected '{list_template[i]}'")
                            raise ValueError
                        print(f"---{content.strip()}---")
                    case 1 | 4 | 7:
                        print(f"Wins: {int(content.strip())}")
                    case 2 | 5 | 8:
                        print(f"Loss: {int(content.strip())}")
    except ValueError:
        #overwrite the existing contents with a template
        print("Unexpected value... Overwriting existing content with basic values")
        with open(user_file, "w") as file:
            for content in list_template:
                file.write(content + "\n")


def user(list_template):
    # Look for the 'users' folder
    # Create the folder if it does not exist
    try:
        users_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users")
        if not os.path.exists(users_dir):
            os.mkdir(users_dir)
            print(f"directory created: {users_dir}")
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None

    # Player enters their username
    # Check to see if that user exists
    # Read the contents of the file to make sure it can be used
    # Create a new file if required
    while True:
        try:
            #Try existing user
            user_name = input("\nEnter your username: ").lower()
            user_file = os.path.join(users_dir, user_name + ".txt") # .txt File path
            read_result(user_file, list_template)
            return user_file
        except OSError:
            #Create a new user
            print(f" The user '{user_name}' does not exist.")
            create_choice = input("Would you like to create a new user? y/n: ").lower()
            if create_choice == "y":
                print("creating your user...\n")
                with open(user_file, "w") as file:
                    #write the existing contents with a template
                    for content in list_template:
                        file.write(content + "\n")
                read_result(user_file, list_template)
                return user_file
        except Exception as e:
            print(f"\n An unexpected error has occurred. Please try again... Reason: {e}")


#def write_result(game, result)
#write to the user file (other scripts use this)
#place values into a list
#'game' will be the name of the actual game ([0]number_guesser [1,2], [3]rock_paper_scissors [4,5], [6]number_sorting [7,8])
#'result' will be a boolean value of true(win) or false(lose)


def main(user_file, list_template):
    print("\n🎮 Welcome to the Game Center! 🎮")

    while True:
        #Help:
        print("\nChoose a game:")
        print("0. Help")
        print("1. Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Sorting Game")
        print("4. Logan's Game")
        print("5. Results")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        #User choices
        #need to somehow parse the 'user_file' argument to these others
        if choice == "0":
            with open("help.txt") as file:
                print(file.read())
        elif choice == "1":
            subprocess.run(["python", "Number Game.py"])
        elif choice == "2":
            subprocess.run(["python", "Rock Paper Scissors.py"])
        elif choice == "3":
            subprocess.run(["python", "Sorting Game.py"])
        #elif choice == "4":
            #subprocess.run(["python", "Sorting Game.py"])
        elif choice == "5":
            read_result(user_file, list_template)
        elif choice == "6":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        
        #Play agin?
        again = input("\nWould you like to play another game? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    list_template = ["Guessing Game", "0", "0", "Rock Paper Scissors", "0", "0", "Sorting Game", "0", "0"] #Basic template of the .txt file
    
    print("🎮 Welcome to the Game Center! 🎮")

    user_file = user(list_template)
    main(user_file, list_template)