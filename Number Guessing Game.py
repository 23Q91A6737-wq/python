# Random Guessing Number game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num , highest_num)
guesses = 0
is_running = True

print("Welcome to the Random Number Guessing Game ")
print(f"Select a number between {lowest_num} and {highest_num}  ")

while is_running:
    guess = input("Enter your Guesses Number: ")
    if guess.isdigit():
        guess=int(guess)
        guesses=guesses+1 #-> or guesses+=1

        if guess < lowest_num or guesses > highest_num:
            print("OUT OF RANGE ! ")

            print(f"Please select the number from {lowest_number} and {highest_num}")

        elif guess < answer:
           print("Too LOW ! , Try Again!")
        elif guess > answer:
           print("Too HIGH ! , Try Again!")
        else:
           print(f"CORRECT ANSWER !!! The answer was {answer}")
           print(f"number of guesses : {guesses}")
           is_running = False

    else:
        print("Invalid ! ")
        print(f"Please select a number between {lowest_num} and {highest_num}")
