import random

def play_game():
    print("Rock, Paper, Scissors Game!")
    print("Choose one: Rock, Paper, or Scissors")
    user_choice = input("Enter your choice: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
play_game()
