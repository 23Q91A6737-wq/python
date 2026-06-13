
# indexing = accessing elements of a sequence using [] (indexing operator )                       the playlist ends in (1:46:17)

#                      [start : end : step]


credit_card_number = "7654-2134-3455-3455"

print(credit_card_number[0])





# Example :- 1


# in this we have [start : end : step]

# if you have to print the starting step

# in below answer we did not include the Dash(-) in the number

# we will not get the answer like 1234-

# instead we will get 1234

credit_card_number = "1234-5678-9012-1234"

print(credit_card_number[0:4] )

# Output :- 1234






# Example :- 2


# or print the indexing number in another way

credit_card_number = "1234-5678-9012-2345"

print(credit_card_number[:4])

# Output :- 1234








# Example :-3


# If you want print middle number

credit_card_number = "1234-5678-9012-2345"

print(credit_card_number[5:9])

# If you want to print the number from middle to end

credit_card_number = "1234-5678-9102-3456"

print(credit_card_number[5:])






# Example :-4


# if you want the last character from the string

#  use negative index

Credit_Card_Number = "1234-5678-9012-3456"

print(Credit_Card_Number[-1])


# Example :-5

# in below example it will count the fifth string form last

credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[::-5])








# Step indexing


# we can access the characters in a string by a given step

# we can count by Two's

# or we can count by Three's

# Example :-6

# If you want to count every second character

credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[::2])

# output :-13-6891-46







# Example :-7

# If you want to count every third character

# if any dashes(-) occurs it will count them and combine the answer

# you can check in below example


credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[::4])

# Output:-  1-814






# Example :-8

# if you want to print the last numebrs

credit_card_number = "2134-5678-9012-3456"

last_digit_number = credit_card_number[-4::]

print(f"XXXX-XXXX-XXXX-{last_digit_number}")






# Example :-9

# If you want to revers the string from last to first

credit_card_number = "1234-5678-9012-3456"

reverse = credit_card_number[::-1]

print(reverse)