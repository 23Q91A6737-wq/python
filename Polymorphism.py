#                            Polymorphism

#  Polymorphism = Greek word means to "have many forms or faces"
#                 Poly = Many
#                 morphe = Form


#       TWO WAYS TO ACHIEVE POLYMORPHISM

#       1. Inheritance = An object could be treated of the same type as a parent class

#        2. "Duck typing" = Object must have necessary attributes/methods

# it is inheritence topic

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius *self.radius # --> pi * r^2

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** self.side

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height

class Pizza(Circle):
    def __init__(self,name,radius):
        super().__init__(radius)
        self.name = name

shapes = [Circle(4),Square(5),Triangle(6,7), Pizza("Dominos",15)]

for shape in shapes:
    print(shape.area())






#• 	An abstract class is like a parent rulebook.
#• 	Inside it, you can define abstract methods (like  or ), which are rules that say: “Every child class must have this method.”
#• 	That means if you create subclasses (Circle, Square, Triangle), they are forced to implement those methods.
#• 	If they don’t, Python will throw an error.
#• 	You cannot directly create an object from the abstract class itself — it’s only a blueprint.

