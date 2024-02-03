import random

# Rock, Paper, Scissors


def get_computer_move(): #random choice generator for computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_player_move(): #player input logic
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. please enter rock, paper, or scissors.")
    return choice


def the_winner(user_choice, computer_choice): #win lose conditions
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "scissors" and computer_choice == "paper") \
        or (user_choice == "paper" and computer_choice == "rock"):
        return "You Win!"
    else:
        return "You Lose!"


def play():
    while True:
        user_choice = get_player_move()
        computer_choice = get_computer_move()
        print(f"\nYou chose: {user_choice}, The computer chose: {computer_choice}")
        result = the_winner(user_choice, computer_choice)
        print(result)

        #play again?
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play()
