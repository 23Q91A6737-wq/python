import random

#help(random)
#print(help)

#number = random.randint(1,20) #-> picks random number from 1 to 20
#print(number)

low = 1
high = 100

number = random.randint(low,high)
print(number)

# if you want a random floating point number
low = 27
high = 77
number=random.random()  #-> to pick a random number in float points
print(number)

# note->

# to print a Rock,Paper,Scissor game

import random

options = ("Rock" , "Paper" , "Sciccor")

option = random.choice(options)

print(option)

# Note ->

#  Deck of cards game

import random

cards = ["2","3","4","5","6","7","8","9","Q","K","J","A"]

random.shuffle(cards) #-> it will shuffle the order of cards

print(cards)

