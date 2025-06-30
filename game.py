import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    choice = input("Your choice: ").lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("==== Rock Paper Scissors Game ====")
    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")
        result = determine_winner(user_choice, comp_choice)
        print(f"Result: {result}")

        again = input("\nPlay again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
