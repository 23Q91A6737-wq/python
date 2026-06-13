# Exercise 2 shopping cart program

item = input("What item would you like to buy ? :  ")

price = float(input("what is the price ? : "))

quantity = int(input("How many would you like to buy ?:  "))

total = price*quantity

print(f"you have bought {quantity} * {item}/s  ")
print(f" the total bill is : ${total} ")