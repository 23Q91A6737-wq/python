# banking program


# 1.show balance
# 2.deposit
# 3.withdraw

'''def show_balance(balance):
    print("***************************")
    print(f"The balance is {balance}")
    print("***************************")

def deposit():
    print("***************************")
    amount = float(input("Enter the amount to be deposited :"))
    print("***************************")

    if amount < 0:
        print("The amount cannot be less than 0")
        return 0
    else:
        return amount

def withdraw(balance):
    print("***************************")
    amount = float(input("Enter the amount to Withdraw :"))
    print("***************************")

    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("The amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance =0
    is_running = True
    while is_running == True:
        print("***************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice = input("Enter the choice (1:4) : ")


        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = balance + deposit()
        elif choice == '3':
            balance = balance - withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("***************************")
            print("please enter a valid choice !!!")
            print("***************************")


    print("***************************")
    print("***************************")
    print("Thank you have a nice day ")
    print("***************************")
    print("***************************")

if __name__ == '__main__':
    main()'''




# Slot Machine Program


'''import random

def spin_row():

    symbols = ['🍒','🍉','🍋','🔔','⭐']

    result = []
    for _ in range(3):
        result.append(random.choice(symbols))
    return result

def print_row(row):
    print(" ".join(row))

def get_payout(row,bet):

    if row[0] == row[1] == row[2]:

        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():

    balance = 100
    print("Welcome to python game ")
    print("Symbols 🍒,🍉,🍋,🔔, ⭐")

    while balance > 0:

        print(f"Current Balance is {balance}")
        bet = input("Enter the amount to bet : ")


        if not bet.isdigit():
            print("Please enter the valid number!!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance ")
            continue

        if bet <= 0:
            print("please enter the amount greater than 0")
            continue

        balance = balance - bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f" congratulations you have won {payout}")
        else:
            print("Sorry you have lost the game")

        balance = balance + payout

        play_again = input("Do you want to play again (Y/N): ")

        if play_again == 'Q':
            break

    print("Thank you ")
    print(f"your final balance is {balance}")


if __name__ == '__main__':
    main()'''




# Encryption Program

'''import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()


print(f"chars : {chars}")
random.shuffle(key)
print(f"key   : {key}")

print()
# encrypt

plain_text = input("Enter a message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f" the original messase : {plain_text}")
print(f" the encrypt message  : {cipher_text}")

# decrypt

cipher_text = input("Enter a message to decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"the encrypt message  : {cipher_text}")
print(f"the decrypted message : {plain_text}")'''


# Hangman Problem


import random

words = ["apple", "orange", "skyblue", "ligthblue", "sea"]
hangman_art = { 0 : ("   ",              # a dictionary where each value pair contains tuple
                     "   ",
                     "   "),
                1 : (" o ",
                     "   ",
                     "   "),
                2 : (" o ",
                     " |  ",
                     "   "),
                3 : (" o ",
                     " |\\",
                     "   "),
                4 : (" o ",
                     "/|\\ ",
                     "   "),
                5 : (" o ",
                     "/|\\  ",
                     "/  "),
                6 : (" o ",
                     "/|\\ ",
                     "/ \\  ")}


def display_man(wrong_guesses):
    
    for i in hangman_art[wrong_guesses]:
        print(i)

def display_hint(hint):
    print(" ".join(hint))

def display_answers(answer):
    print(" ".join(answer))

def main():

    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a guess : ")
        
        if guess != 1 or not guess.isalpha():
            print("Invalid answer")
            continue
        guessed_letters.add(guess)  #

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("YOU WIN")
            is_running = False
        
        elif wrong_guesses > len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_hint(hint)
            print("YOU LOSE")
            is_running = False






if __name__ == '__main__':
    main()



