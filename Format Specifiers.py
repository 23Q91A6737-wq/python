
# Format Specifiers

# formant specifiers = { value : flags} format a value based on what
#                                  flags are inserted

# .(number)f = round to that many decimals places (fixed point)

# :(number) = allocate that many spaces

# :03 = allocate and zero pad that many spaces

# :< = left justify

# :> = right justify

# :^ = center align

# :+ = use a plus to indicate positive value

# :=  = place sign to leftmost position

# :  = insert a space before positive numbers

# :, = comma separator



# Example :-1

#formant specifiers = { value : flags} format a value based on what
#                                  flags are inserted

price1 = 2.789654
price2 = 23.6587
price3 = 10147

print(f"The price 1 is {price1:.2f}")

print(f"The price 2 is {price2:.2f}")

print(f"The price 3 is {price3:.2f}")

# Output :-
#The price 1 is 2.79
#The price 2 is 23.66
#The price 3 is 10147.00








# Example :- 2

# :(number) = allocate that many spaces

car_tata = 963987.235
car_hyundai = 9874521.3215
car_mercedes = 32145887.32145

print(f" The price of a Tata car {car_tata:23}")

print(f" The price of a Hyundai car is {car_hyundai:27}")

print(f" The price of a Mercedes car si {car_mercedes:30}")

# Output


#The price of a Tata car              963987.235
#The price of a Hyundai car is                9874521.3215
#The price of a Mercedes car si                 32145887.32145








# Example :- 3

# :(number) = allocate that many spaces

car_tata = 963987.235
car_hyundai = 9874521.3215
car_mercedes = 32145887.32145

print(f" The price of a Tata car {car_tata:}")

# after print(f" The price of a Tata car {car_tata:-> in this insert any value(number) it leave that much space)

print(f" The price of a Hyundai car is {car_hyundai:}")

print(f" The price of a Mercedes car si {car_mercedes:}")

# Output
#The price of a Tata car 963987.235
#The price of a Hyundai car is 9874521.3215
#The price of a Mercedes car si 32145887.32145









# Example :- 4

# # :< = left justify

# moves the value(number which you have inserted) into <- left side

# if space is leaved


chips_price = 50.2555

drink_price = 40.258

snacks_price = 123.0258

print(f" The chips price is {chips_price:<10}")

print(f" The drink_price is {drink_price:<10}")

print(f" The snacks price is {snacks_price:<10}")

# Output

# The chips price is 50.2555
#The drink_price is 40.258
#The snacks price is 123.0258










# Example :- 5

## :> = right justify

#  it moves the value(number you have inserted in { price : >26 }-> moves to right side

# according to the value in above example 26 value.


booksv_price = 1234567

penv_price = 20.656

print(f"The price of the booksv is {booksv_price:>10} ")
print(f" The price of the penn is {penv_price:>10}")

# Output

# The price of the booksv is    1234567
# The price of the penn is     20.656










# Example :- 6

## :^ = center align

# it will assign the value to the center

Windows_Laptop = 12356.025478

MacOs_Laptop = 63255.321456

Zebronics_Laptop = 254.325

print(f" The price of the Windows Laptop     ${Windows_Laptop:^10}")

print(f" The price of the Apple MacOs Laptop ${MacOs_Laptop:^10}")

print(f" The price of the Zebronics Laptop   ${Zebronics_Laptop:^10}")

# Output

#The price of the Windows Laptop       $12356.025478
#The price of the Apple MacOs Laptop   $63255.321456
#The price of the Zebronics Laptop     $ 254.325  (-> the 254 value came to the middle leaving space  in doewn of 6 ($63255.321456)













# Example :- 7

# # :+ = use a plus to indicate positive value

# in simple words it multiply the value with +

# ( + * + = +) (plus into plus = +)

# ( + * -) ( plus into minus = -)

# for a positive value = 2134    -> after doind the operation -> +2134   (because + * + = +)   (plus into plus = +)

# for a negative value = -789     -> after doing the operation -> -789   (because - * + = -)   (minus into plus = -)

credit_card_balance = 12320.654

bank_balance = 12336.2254

monthly_EMI = -1236.369

print(f"The Credit card balance is       ${credit_card_balance:+}")

print(f"The Bank balance is              ${bank_balance:+}")

print(f"The monthly EMI charges is       $ {monthly_EMI:+}")

# Output
#The Credit card balance is       $  +12320.654
#The Bank balance is              $  +12336.2254
#The monthly EMI charges is       $  -1236.369














# Example :-8

# by  using the camma (,) . each thousand's place is now

# separated with a comma

car_price = 123600.545

bike_price = 12309.6578

cycle_price = 1250.05445

print(f"The proce of the car is {car_price:,}")

print(f"The price of the bike is {bike_price:,}")

print(f"The price of the cycle {cycle_price:,}")

# Output
#The proce of the car is 123,600.545
#The price of the bike is 12,309.6578
#The price of the cycle 1,250.05445












# Example :- 9

# in the below example we solve the problem 

# using the ( + , .2f ) operators

suv_price = 78945.32145

hachback_price = 45632.3210

suden_price = 12320.325563

print(f" The price of the SUV car is {suv_price:+25,.2f}")

print(f"The price of the Hachback car is {hachback_price:+21,.3f}")

print(f"The price of the Suden car is {suden_price:+24,.4f}")

# Output

 #The price of the SUV car is                +78,945.32
#The price of the Hachback car is           +45,632.321
#The price of the Suden car is             +12,320.3256