# default arguments

# default = A default value for certain parameters
#           default is used when that argument is omitted
#           make your functions more flexible, reduce # of arguments
#           1.positional, 2. DEFAULT, 3.keyword 4. arbitrary

def net_price(list_price,discount,tax):
    return list_price * (1- discount) * (1+tax)

print(net_price(500,0,0.05))

# or in another method

def net_price(list_price, discount =0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))

print(net_price(500, 0.1,0))  # if 10% percent coupon is applied


# Exercise - 1


# method 1

import time

def count(start,end):
    for x in range(start,end):
        print(x)
        time.sleep(1)
    print("Done!")

count(0,2)


# Exercise -1

# another method

import time

def count(end ,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(4)

# Exercise

# another method

import time

def count(end ,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(27,17)

