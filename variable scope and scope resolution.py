
# variable scope and scope resolution           (05:09:21) -> playtime BroCode


# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

print("---------------------------------------------------------------")

# the below answer is error because the function cannot see other functions


'''  def func1():
      a = 1
      print(b)

def func2():
    b = 2
    print(b)       '''

# Note ->

# function cannot see of other functions , but they can see inside of their own function.

# that's why we sometimes pass arguments to  . so that our functions are aware of them

# using this concept , we could create different versions of the same variables.

# Let's rename a to be X and b to be X as well.



# Local

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

print("---------------------------------")
# the local version of x found within function one and a local version of x found within function two.

# whenever we utilize a variable , we will first look to see if there's any local instance of that variable.

# if there isn't, we would move to the enclosed scope.

#---------------------------------------------------------------------

# Enclosed

# with an enclosed scope

def func1():
    x =1


    def func2():
        x = 2
        print(x)
    func2()

func1()

print("-------------------------------")

def func1():
    x =1


    def func2():
        print(x)
    func2()

func1()

print("------------------------------------------")

# Global scope

# Global meaning is outside of any functions

# i will eliminate these variable declarations

def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

# we are printing 3 twice
# once for func1 and once for func2
# there is no longer version of X for both these functions.

print("-----------------------------------------------------------------")




# Built-in

from math import e

# e is built-in

def func1():
    print(e)

func1() # invoke func1()

print("---------------------------------------------")

# Example -> 2

from math import e

def func1():
    print(e)

e = 3

func1()

# note ->

# if I set to E to be a different value like three, what we're doing technically is creating is two different versions of E

# Variables can share the name as long as they're within a different scope.

# we have a built-in version of E and global version of E.

# if it was to print E now , it would print my global version

# Because using the LEGB order,

# we would first look for any local scope of E ,

# then Enclosed scope

# then Global, which we do have one of E=3

# then lastly Built-in