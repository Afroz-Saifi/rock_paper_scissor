import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice in ('rock', 'paper', 'scissors', 'q'):
            return user_choice
        print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'q' to quit.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0
    draws = 0

    print("Let's play Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()

        if user_choice == 'q':
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            draws += 1
            print("It's a draw!")

        print(f"Score: You {user_score} - {computer_score} Computer ({draws} draws)\n")

    print("Thanks for playing! Final Score:")
    print(f"You: {user_score} - Computer: {computer_score} ({draws} draws)")

if __name__ == "__main__":
    main()
