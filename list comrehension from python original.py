# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]


# Example -> method -> 1

doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

print("------------------------------------------")
# method -> 2
# Example ->1


# [expression for value in iterable if condition] -> this formula in used in future. for now use the below formula

# [expression for value in iterable ]
#  ----------     -----    --------
#     [expression|  for  |value|  |in|   |iterable| ]
triples =[x * 3     for    x        in       range (17,27)]
#triples =[x * 3 for x in  range (17,27)]
print(triples)

print("---------------------------------------------------")
# Example -> 2

# method ->1
fruits = ["apple", "banana", "pineapple", "orange"]

fruits = [fruit.upper() for fruit in fruits]

print(fruits)

print("-----------------------------------")


# method ->2

fruits = [fruit.upper() for fruit in ["apple", "banana", "orange", "beetroot"]]

print(fruits)

print("-----------------------------------------------------")

# indexing

fruits = ["apple", "orange", "beetroot", "watermelon"]

fruit_charts = [fruit[0] for fruit in fruits]
print(fruit_charts)

print("--------------------------------------------------")

# using if conditions also
#[expression for value in iterable if condition]

numbers = [1,-2,3,-4,5,-6,8,-7]

positive_numbers = [num for num in numbers if num >= 0]

print(positive_numbers)

negative_numbers = [num for num in numbers if num <= 0]

print(negative_numbers)

odd_numbers = [num for num in numbers if num % 2 == 1]  # num % 2 == 1 . that means that number doesn't divide by 2 evenly

print(odd_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

print()

print("--------------------------------------")

print()

# Example -> 2

marks = [100,45,87,97,65,89,78]

good_numbers= [mark for mark in marks if mark >= 77]

print(good_numbers)