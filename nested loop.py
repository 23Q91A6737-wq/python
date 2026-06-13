# nested loop = The "inner loop" will finish all of it's iterations before

#                finishing one iteration of the "outer loop"

# nested loop = A loop within another loop (outer,inner)

#                   outer loop:
#                      inner loop:



# Example ->1
for x in range (1,4):
    for y in range(1, 10):
        print(y, end="-")
    print()# this outer loop would just print a new line







rows = int(input("How many rows? : "))

columns = int(input("How many columns? : "))

symbol = input("Enter a symbol to use : ")

for i in range(rows):

    for j in range(columns):

        print(symbol,end=" ")

    print()