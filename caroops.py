
# we will create a class of Car

#  we will create some Car objects (class Car:)

# to construct a car object we need a special type of method called a constructor
#
# this is our constructor method (__init__(self))

# we need this method to construct or create the objects

# this method behaves simliar to the function

# self means this object we are creating right now

# we need to set up the parameters

# and what are the attributes that a student should have __init__(self,name,year,rollno)

class Car:

    def __init__(self, model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
