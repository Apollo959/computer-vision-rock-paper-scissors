import random

options = ["Rock","Paper","Scissors"]

def get_computer_choice(options):
    return random.choice(options)

def get_user_choice():
    choice = input("Rock, Paper, Scissors, go!:\n")
    return choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a draw!")
    elif computer_choice == "Rock" and user_choice == "Scissors" or computer_choice == "Scissors" and user_choice == "Paper" or computer_choice == "Paper" and user_choice == "Rock":
        print("Computer wins!")
    else:
        print("Human wins!")

def play(options):
    comp_choice = get_computer_choice(options)
    human_choice = get_user_choice()
    get_winner(comp_choice, human_choice)

play(options)