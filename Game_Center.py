import os
import subprocess


#WRITE RESULTS: Modify the save file
#RETURNS: None
def write_result(game_id, result, user_file):
    #write to the user file (other scripts use this)
    #place values into a list
    #'game_num' will be the dedicated number of the actual game (1-number_guesser [0][1,2], 2-rock_paper_scissors [3][4,5], 3-number_sorting [6][7,8])
    #'result' will be a boolean value of true(win) or false(lose)
    
    list_file_content = read_result(user_file)
    match game_id:
        case 1: #Number Guesser game
           if result == True:
                list_file_content[1] = int(list_file_content[1]) + 1
           elif result == False:
                list_file_content[2] = int(list_file_content[2]) + 1
        case 2: #Rock Paper Scissors game
            if result == True:
                list_file_content[4] = int(list_file_content[4]) + 1
            elif result == False:
                list_file_content[5] = int(list_file_content[5]) + 1
        case 3: #Sorting game
            if result == True:
                list_file_content[7] = int(list_file_content[7]) + 1
            elif result == False:
                list_file_content[8] = int(list_file_content[8]) + 1
    #print(list_file_content) #Debug
    
    #Write the file with updated results
    with open(user_file, "w") as file:
            for content in list_file_content:
                file.write(str(content) + "\n")


#READ RESULTS: Ensures the integrity of the save file
#RETURNS: A list of the save file content
def read_result(user_file):
    #place values in a list
    #print out results
    global list_template
    
    list_file_content = []

    try:
        #ensure the contents of the file are as expected
        with open(user_file) as file:
            for i, content in enumerate(file.readlines()):
                list_file_content.append(content.strip())
                match i:
                    case 0 | 3 | 6:
                        if content.strip() != list_template[i]:
                            print(f"'{content.strip()}' Does not exist... Expected '{list_template[i]}'")
                            raise ValueError
                    case 1 | 4 | 7:
                        int(content.strip())
                    case 2 | 5 | 8:
                        int(content.strip())
                if i >= 8:
                    break
        while len(list_file_content) < 9:
            #print("less than 9")
            list_file_content.append("0")
            with open(user_file, "a") as file:
                file.write("\n0")
    except ValueError:
        #overwrite the existing contents with a template
        print("Unexpected value... Overwriting existing content with basic values")
        with open(user_file, "w") as file:
            for content in list_template:
                file.write(content + "\n")
        list_file_content = list_template
    #print(list_file_content)
    return list_file_content #returns the list. Keep in mind everything is already stripped


#USER: Sets up the players save files, creates or overwrites as required
#RETURNS: A list containing [0] = Username || [1] = Save file directory
def user():
    global list_template
    
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
            list_file_content = read_result(user_file)
            
            print(f"\nYour current results are:")
            for i, content in enumerate(list_file_content):
                match i:
                    case 0 | 3 | 6:
                        print(f"---{content}---")
                    case 1 | 4 | 7:
                        print(f"Wins: {content}")
                    case 2 | 5 | 8:
                        print(f"Loss: {content}")
            return [user_name, user_file]
        except FileNotFoundError:
            #Create a new user
            print(f" The user '{user_name}' does not exist.")
            create_choice = input("Would you like to create a new user? y/n: ").lower()
            if create_choice == "y":
                print("creating your user...\n")
                with open(user_file, "w") as file:
                    #write the existing contents with a template
                    for content in list_template:
                        file.write(content + "\n")
                read_result(user_file)
                return [user_name, user_file]
        except Exception as e:
            print(f"\n An unexpected error has occurred. Please try again... Reason: {e}")


#MAIN: The hub to access other applications from
#RETURN: None
def main():
    print(f"\n🎮 Welcome {user_file[0]}!  🎮")

    while True:
        #Help:
        print("\nChoose a game:")
        print("0. Help")
        print("1. Shopping Cart (Jin)")
        print("2. Guessing Game (Jin)")
        print("3. Rock Paper Scissors (Lys)")
        print("4. Sorting Game (Barry)")
        print("5. Colour Guesser (Logan)")
        print("6. Results")
        print("7. Exit")
        choice = input("Enter your choice (1-6): ").lower()

        #User choices
        #need to somehow parse the 'user_file' argument to these others
        match choice:
            case "0" | "help":
                with open("help.txt") as file:
                    print(file.read())
            case "1":
                subprocess.run(["python", "List_Shopping_Cart.py"])
            case "2":
                subprocess.run(["python", "number_game.py", user_file[1]])
            case "3":
                subprocess.run(["python", "rock_paper_scissors.py"])
            case "4":
                subprocess.run(["python", "sorting_game.py", user_file[1]])
            case "5":
                subprocess.run(["python", "colour_guesser.py"])
            case "6" | "result" | "results":
                print(f"\nYour current results are:")
                with open(user_file[1]) as file:
                    for i, content in enumerate(file.readlines()):
                        match i:
                            case 0 | 3 | 6:
                                print(f"---{content.strip()}---")
                            case 1 | 4 | 7:
                                print(f"Wins: {content.strip()}")
                            case 2 | 5 | 8:
                                print(f"Loss: {content.strip()}")
                        if i >= 8:
                            break
            case "7" | "exit":
                print("Thanks for playing. Goodbye!")
                break
            case _:
                print("Invalid choice. Try again.")
        
        #Play agin?
        again = input("\nWould you like to play another game? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing. Goodbye!")
            break



list_template = ["Guessing Game", "0", "0", "Rock Paper Scissors", "0", "0", "Sorting Game", "0", "0"] #IMPORTANT: Basic template of the .txt file
if __name__ == "__main__":
    print("🎮 Welcome to the Game Center! 🎮")

    user_file = user() #IMPORTANT: Stores a list <||>   [0] = user_name   ||   [1] = [This program's directory]\users\[user].txt <||>
    main()
