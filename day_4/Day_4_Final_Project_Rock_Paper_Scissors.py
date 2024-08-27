import random
game_choice = ["rock","paper","scissors"]
user_choice = input("What do you choose? Rock, Paper or Scissors? Enter your choice - ")
computer_choice = random.choice(game_choice)
print(f"You choice - {user_choice} \nComputer choice - {computer_choice}")
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Computer win, you lose")
    else:
        print("You win")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("Computer win, you lose")
    else:
        print("You win")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Computer win, you lose")
    else:
        print("You win")
elif user_choice != "rock" or user_choice != "paper" or user_choice != "scissors":
    print("You made the wrong choice")
