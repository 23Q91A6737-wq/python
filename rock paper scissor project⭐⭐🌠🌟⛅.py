# Rock Paper Scissor Game

import random

options = ("rock" , "paper" , "scissor")
is_running = True

while is_running:

    player = None
    computer = random.choice(options)

    while player not in options:

        player = input("Enter a selection of (rock , paper , scissor) : ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("Its a Tie  😅 !!!")

    elif player == "rock" and computer == "scissor":  # -> LOGICAL OPERATOR
        print("Player Wins 😎")

    elif player == "scissor" and computer == "paper":
        print("player wins 😎")

    elif player == "paper" and computer == "rock":
        print("player wins 😎")

    else:
        print("player lose 🤧")

    is_running = input("play again ? : ").lower()
    if not is_running == "y":
        is_running = False
        print("thank you !! Bye 😏!! ")




