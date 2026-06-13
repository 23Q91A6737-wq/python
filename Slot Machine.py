# Slot Machine Program          (5:38:34) Brocode

import random

def spin_row():
    symbols  = ['🍒', '🍉', '🍋', '🔔', '⭐' ]

    #results=[]

    #for symbol in range(3):
     #   results.append(random.choice(symbols))
    #return results

    # or you can use list comprehension

    return[ random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**********************")
    print(" ".join(row))        # so we need set one parameter [from print_row before . after -> print_row(row)] our row that we receive . It's going to be a list.,
    print("**********************")   #  i will just create a space
                              # with strings they are built-in methods
                              # we will use the join method then pass in our list or other iterable.
                                 # basically what we're saying using the join we're going to take our iterable in this case our list join each element by a space . a space character

# you can  use print(" | " .join(row))

def get_payout(row, bet):

    if row[0] == row [1] == row[2]:

        if row[0] == '🍒':     # you can choose even  any row also like row[1] and row[2] also , because row[0] == row[1] == row[2]
            return bet * 3
        if row[0] == '🍉':    # you can choose even  any row also like row[1] and row[2] also , because row[0] == row[1] == row[2]
            return bet * 4
        if row[0] == '🍋':    # you can choose even  any row also like row[1] and row[2] also , because row[0] == row[1] == row[2]
            return bet * 5
        if row[0] == '🔔':    # you can choose even  any row also like row[1] and row[2] also , because row[0] == row[1] == row[2]
            return bet * 10
        if row[0] == '⭐':     # you can choose even  any row also like row[1] and row[2] also , because row[0] == row[1] == row[2]
            return bet * 20

    return 0


def main():
    balance = 1000

    print("*****************")
    print("Welcome to Python Slots Machine")
    print("Symbols : 🍒 🍉 🍋 🔔 ⭐ ")
    print("*****************")

    while balance >0:
        print(f"Current balance : ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
          # converting digit to integer by type-casting method
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()   #->this function is going to return a list which we assign to be row.
        # 2)  row will be a list,
        # 3) using the spin row function, we have to generate three random symbols then return them within a list.
        print("Spinning...\n")
        print_row(row)   # we will pass in one argument , our row,
        # that's returned to us after we spin the row.

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"you won $ {payout}")
        else:
            print("Sorry you lost this round")

        balance = balance + payout

        play_again = input("Do you want to use again (Y/N) : ").upper()

        if play_again == 'Q':
            break

    print("**********************************************")
    print(f"Game over ! your final balance is ${balance}")
    print("***********************************************")


if __name__ == '__main__':
    main()