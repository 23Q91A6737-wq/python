# Hangman in python

import random
words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:()   @ we will have a key  which will bw a number and tuple.
                           # the key is going to represent the incorrect number of guesses.

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



def display_man(wrong_guesses):   # the incorrect guesses print the lines for example one incorrect guess print 'o'

    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):    # the right guesses , we will flip one of those underscores to be a letter if that letter is correct. the hint contains list like [_, _, _, _, _, _,_,]
    print(" ".join(hint))

def display_answer(answer):  # display the correct answer either when we lose the game or win the game.
    print(" ".join(answer))

def main(): # it contains the main body of code of our program

    answer = random.choice(words)   # it will choose random choice from the words
    hint = ["_"] * len(answer)      # it will print the ['_' , '_'] according the length of the word from the random choice of the answer
    wrong_guesses = 0
    guessed_letters = set()     #Start with an empty record of letters guessed # going to keep track of all the incorrect guesses that we have made . we will create a sat of guesses letters.for an empty set , we will call the set function. Normally in python  we create the set function like -> [set()]
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter : ").lower()

        if len(guess) != 1 or not guess.isalpha():  # if the length does not equal to 1 (means some people enter whole word at a time like "apple" or two words "ap" ) it will print Invalid answer and if anyone enters integers other than alphabets also it will print Invalid Answer.
            print("Invalid output")
            continue
        guessed_letters.add(guess)  #Store the player’s guessed letter (no duplicates)

        if guess in answer:                #Check if the guessed letter is in the secret word
            for i in range(len(answer)):  # Go through every letter of the secret word # here i means index
                if answer[i] == guess:     #Check if the current letter matches the guessed letter
                    hint[i] = guess          #  Reveal the correct letter in the hint list
        else:
            wrong_guesses += 1

        if ("_") not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You have won the game")
            is_running = False


        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose")
            is_running = False

if __name__ == '__main__':
    main()