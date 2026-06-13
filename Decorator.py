#       Decorator

# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("* You should add sprinkles *")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs): #       *args,kwargs --> to accept any number of arguments and keyword arguments (Args,kwargs)
        print("you should add fudge")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"here is your {flavour} ice cream")

get_ice_cream("vanilla")


'''🎯 Key Point
- *args = collects all positional arguments (like "vanilla").
- **kwargs = collects all keyword arguments (like flavour="vanilla").
- Together, they make the wrapper flexible — it can decorate any function, no matter how many arguments it takes.
'''