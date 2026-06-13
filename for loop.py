# for loops =  execute a  block of code a fixed number of times.

#              you can iterate over a range, string, sequence, etc.


# Example :-1

for x in range ( 0, 11):


    print(x)

print("Get set go !")

# Example :- 2  (reverse loop)

# if you want a reverse for loop

for x in reversed(range(0,11)):

    print(x)

print("Happy Ugadi")


# Example :- 3 (step function)

# if you want step function

# it is used in odd , even and some other operators



# Example :-3 (even numbers using step function)


# the below example shows even numbers

for i in range(0,11,2):

    print(i)

# Example :- 4  (odd numbers)

# the below example shows odd numbers
for i in range(1,11,2):

    print(i)


# Example :-4 (using '3' step function)

# if you want to change the step to three

# you would count by threes

for i in range(21,57,3):

    print(i)

# Example :- 5

# in this function you can also iterate over a string

credit_card_number = "9876-5432-1098-7654"

for x in credit_card_number:

    print(x)




# Example :- 6 (using continue method)

# for loops using continue

# for skip over an iteration ,  you can use the continue keyword

# by using this process the below example

for i in range(1,17):

    if i == 11:

        continue

    else:
        print(i)



# Example :- 7 (using break-out method to escape the loop)

# in the below example

# we will break out of this loop entirely

for x in range(0,23):
    if x == 17:

        break

    else:
        print(x)


# Example :- 8 (to print the output in one line)

for i in range(0,11):

    print(i,end = "")

# Example :- 9 ( to print the ouput in one line with spaces)

# type space between the double coloumns

for x in range(0,7):

    print(x,end = " ")

# Example :-9

# in this below example

# when you type something in between the double quotes

# it will appear as it is shown below (-)

for y in range(0,7):

    print(y,end = "-")


# Note :-

# you can execute a block of code a fixed number of times.

# there is a lot of overlap where you could use either a while loop or a for loop.

# while loops tend to be better if you need to execute something possibly infinite amount of times,

# for example such as accepting user input

