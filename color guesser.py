import random

def letters_in_common(a, b):
    return len(set(a) & set(b))

def color_guessing_game():
    colors = [
        'red', 'blue', 'green', 'yellow', 'purple', 'orange',
        'pink', 'brown', 'black', 'white', 'gray', 'cyan',
        'magenta', 'lime', 'teal', 'navy', 'maroon', 'olive',
        'gold', 'silver'
    ]

    total_guesses = 0
    correct_guesses = 0

    print("Welcome to the Color Guessing Game!")
    print("Type the name of the color I am thinking of.")
    print("Type 'quit' or 'exit' anytime to leave the game.")

    while True:
        chosen_color = random.choice(colors)
        # Start guessing loop until correct
        while True:
            guess = input(f"Guess the color ({', '.join(colors)}): ").strip().lower()

            if guess in ["quit", "exit"]:
                print(f"\nThanks for playing! You got {correct_guesses} correct out of {total_guesses} guesses!")
                print("Goodbye!")
                return

            if guess not in colors:
                print("Invalid color. Please try again.")
                continue

            total_guesses += 1

            if guess == chosen_color:
                correct_guesses += 1
                print("Correct! 🎉")
                break  # exit guess loop, pick a new color
            else:
                print("Wrong!")
                hint = ""
                if guess[0] == chosen_color[0]:
                    hint = f"Hint: Your guess and the color start with the same letter '{guess[0]}'."
                else:
                    common_letters = letters_in_common(guess, chosen_color)
                    length_diff = len(chosen_color) - len(guess)
                    length_hint = ""
                    if length_diff > 0:
                        length_hint = f" The color is {length_diff} letter{'s' if length_diff > 1 else ''} longer than your guess."
                    elif length_diff < 0:
                        length_hint = f" The color is {abs(length_diff)} letter{'s' if abs(length_diff) > 1 else ''} shorter than your guess."

                    hint = f"Hint: Your guess and the color share {common_letters} letter{'s' if common_letters != 1 else ''}.{length_hint}"

                print(hint)

if __name__ == "__main__":
    color_guessing_game()

