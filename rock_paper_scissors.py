import random

# Rock, paper and scissors in the list
choices = ["rock", "paper", "scissors"]

# Random thing from the list
choice = random.choice(choices)

# User input
user_choice = input("Rock, paper or scissors? ").lower()

# The game rolls
def rockPaperScissors():
    if user_choice == "rock":
        if choice == "rock":
            print("Rock")
            print("It's a draw!")
        elif choice == "paper":
            print("Paper")
            print("The computer wins!")
        else:
            print("Scissors")
            print("You win!")

    elif user_choice == "paper":
        if choice == "rock":
            print("Rock")
            print("You win!")
        elif choice == "paper":
            print("Paper")
            print("It's a draw!")
        else:
            print("Scissors")
            print("The computer wins!")
            
    elif user_choice == "scissors":
        if choice == "rock":
            print("Rock")
            print("The computer wins!")
        elif choice == "paper":
            print("Paper")
            print("You win!")
        else:
            print("Scissors")
            print("It's a draw!")
    else:
        print("Please input rock, paper or scissors!")

rockPaperScissors()