# Dice Roller Program             (03:42:47)-> playtime BroCode
import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")  #-> THESE are seven unique code characters

# to print ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = { 1: ("┌─────────┐" ,                             #creating dictionary
                 "│         │" ,
                 "│    ●    │" ,
                 "│         │" ,
                 "└─────────┘"  ),

             2 :("┌─────────┐" ,
                 "│ ●       │" ,
                 "│         │" ,
                 "│       ● │" ,
                 "└─────────┘" ),

             3 :("┌─────────┐" ,
                 "│ ●       │" ,
                 "│    ●    │" ,
                 "│       ● │" ,
                 "└─────────┘" ),

             4 :("┌─────────┐" ,
                 "│ ●     ● │" ,
                 "│         │" ,
                 "│ ●     ● │" ,
                 "└─────────┘" ),

             5 :("┌─────────┐" ,
                 "│ ●    ● │" ,
                 "│    ●    │" ,
                 "│ ●     ● │" ,
                 "└─────────┘" ),

             6 :("┌─────────┐" ,
                 "│ ●     ● │" ,
                 "│ ●     ● │" ,
                 "│ ●     ● │" ,
                 "└─────────┘" ),
             }


dice = []

total = 0

num_of_dice = int(input("Enter the number of dice: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
print(dice)

# if you prefer answer vertical you can go with the below code

# for die in dice:
#   for line in dice_art.get(dice[die]):
#       print(line )

 # if you prefer answer in horizontal . follow the below code

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line] , end="")
    print()
total = total + die
print(f"total : {total}")





