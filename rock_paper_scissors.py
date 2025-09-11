#Lys
import random 
def rock_paper_scissors(): 
    choices = ["rock", "paper", "scissors"] 
    user_choice = input("Choose rock, paper, or scissors: ").lower() 
    if user_choice not in choices: 
        print("Invalid choice.") 
        return None  # invalid input, no score change 
    computer_choice = random.choice(choices) 
    print(f"Computer chose: {computer_choice}") 

    if user_choice == computer_choice: 
        print("It's a tie!") 
        return 0 
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"): 
        print("You win this round!") 
        return 1 
    else: 
        print("Computer wins this round!") 
        return -1 

# Play until a sole winner is found 

while True: 

    player_score = 0 
    computer_score = 0 
    rounds = 5 
    current_round = 0 

    print("\n--- Rock Paper Scissors: Best of 5 ---\n") 
    while current_round < rounds: 
        print(f"Round {current_round + 1}") 
        result = rock_paper_scissors() 

        if result == 1: 
            player_score += 1 

        elif result == -1: 
            computer_score += 1 

        elif result is None: 
            continue  # don't count invalid inputs 
        current_round += 1 

        print(f"Score -> You: {player_score}, Computer: {computer_score}\n") 

    # After 5 rounds, check if we have a sole winner 
    print("Set finished!") 

    if player_score > computer_score: 
        print("🎉 You win the game!") 
        break 
    elif player_score < computer_score: 
        print("💻 Computer wins the game!") 
        break 
    else: 
        print("🤝 It's a tie set! Playing another 5 rounds...\n") 
