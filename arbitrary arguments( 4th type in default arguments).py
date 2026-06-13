# * args      =   allows you to pass multiple non-key arguments
#**kwargs   =   allows you to pass multiple keyword-arguments
#               * unpacking operator
#               1.positional 2.default 3.keyword  4.ARBITRARY

# args    ->   full form is  "arguments".
# kwargs  ->   full form is  "keyword arguments".
def display_name(*args):
    for arg in args:
        print(arg,end=" ")

# with the unpacking operator(*) followed by a unique parameter name(args) . you can pack all of these arguments into a tuple . which you can use this function
display_name("Dr.","Spongebob","squarepants","III")
print("\n\n\n")

# now we will discuss next topic  **kwargs

def print_address(**kwargs):
    #print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_address(street="pedhamma thalli colony",
              apartmentno="101",
              city="Nizambad",
              state="Telengana",
              pincode="500300")

print("---------------------------------------\n\n")

# Exercise -1 (using both args and kwargs)


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('pincode')}")
shipping_label("Dr.","Spongebob","Squarepants","V",
               street="pedhamma Thalli colony",
               apartment="101",
               city="NZB",
               state="Telangana",
               pincode="503003")


print("---------------------------------\n\n\n")

# Exercise -1 (Full Version)

def shipping_label(*args,**kwargs):

    for arg in args:
        print(arg,end=" ")
    print()

    if "apartment" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('pincode')}")
shipping_label("Dr","Spongebob","Squarepants","V",
               street="pedhamma Thalli Colony",
               apartment="101",    # or you can choose PO BOX = #7007
               city="NZB",
               state="Telangana",
               pincode="503003")

print("----------------------------------------------------------------------")