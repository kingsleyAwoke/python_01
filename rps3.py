import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("Enter...\n1 for Rock,\n2 forPaper or\n3 for scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()
    

    player = int(playerchoice)


    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("You choose " + str(RPS(player)).replace("RPS", ",") + ".")
    print("Python choose " + str(RPS(computer)).replace("RPS", ",") + ".")

    if player == 1 and computer == 3:
        print("You win! 🙌")
    elif player == 2 and computer == 1:
        print("You win! 🙌")
    elif player == 3 and computer == 1:
        print("You win! 🙌")
    elif player == computer:
        print("Tie game! 👊")
    else:
        print("Python wins! 🐍")

    print("\nPlay again?")

    while True:
        playagain = input("\nY for yes\n Q for quit\n")

        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🙌🙌 Thank you for playing\n")
        sys.exit("Bye 😒")


play_rps()