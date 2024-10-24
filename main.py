import random

'''
1 for snake
-1 for water
0 for gun
'''

# Random choice by computer
computer = random.choice([-1, 0, 1])

# User input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Choice dictionaries
youDict = {"s": 1, "w": -1, "g": 0}
reverseDist = {1: "snake", -1: "water", 0: "gun"}

# Input validation
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    # Get user's choice
    you = youDict[youstr]

    # Show choices
    print(f"You chose {reverseDist[you]}\nComputer chose {reverseDist[computer]}")

    # Determine the winner
    if computer == you:
        print("It's a draw!")
    else:
        if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You win!")
        else:
            print("You lose!")
