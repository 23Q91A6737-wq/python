# Shopping Cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter your food to buy (q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: ₹"))
        foods.append(food) # -> append =  is used to add thenew item in the list[]
        prices.append(price)
        total += price

print("\n--------- YOUR CART ---------")

print()  # -> is used to print another line

for i in range(len(foods)):
    print(f"{i + 1}. {foods[i]} - ₹{prices[i]}")

print(f"\nYour total is ₹{total}")

