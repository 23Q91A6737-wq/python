# Super Function

# super() = Function used in a child class to call methods from a parent class (superclass).
#           it Allows you to extend the functionality of the inherited methods

# the child class is the subclass.

# the parent class is the super class

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} and it is {'filled' if self.is_filled else 'not filled' } ")   #-> it is like ( 'condition' if 'condition' else 'condition') it is if else in another form


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f" it is a circle with an area of {3.14 * self.radius *self.radius}cm^2")  #   for overriding the method              # --> area of circle = pi * r^2


        super().describe()  # to access the method from the parent class also   ,,,,,,, because if you not use this method it not show parent output like   "it is red and it is filled "

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


    def describe(self):
        print(f" the area of the triangle is {self.width*self.height/2}cm^2")   # area of the triangle is ---> 1/2 * base *height
        super().describe()


# Create objects
circle = Circle(color="red",is_filled= True,radius= 5)
square = Square("orange", False, 4)
triangle = Triangle("blue", True, 5, 4)

# Print values
print(circle.color)
print(circle.is_filled)
print(circle.radius)
print()

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
print()

print(triangle.color,triangle.is_filled, triangle.width, triangle.height)
print()

# def describe


circle.describe()  # it will give two ouputs one is from parent class method and other is from child method

print()

square.describe()

print()

triangle.describe()

