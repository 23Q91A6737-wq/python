# Concession Program

menu = { "Veg pizza" : 7.00,
         "Burger" : 6.50,
         "Coca-Cola": 2.27,
         "Thumbs-Up": 5.20,
         "Chips" : 4.50,
         "lemonade": 2.25,
         "Dominos" : 5.57}

cart = []    #-> it is the user selection

total = 0

print("-------MENU-------")

for key,value in menu.items():
    print(f"{key:10} : ${value}")

print("------- -------")

while True:
    food = input("Select your item from Menu (q to quit) : ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)



print("-------YOUR ORDER-------")


for food in cart:
    total = total+ menu.get(food)
    print(food,end=" " )

print()

print(f"your total is : {total:.2f}")

