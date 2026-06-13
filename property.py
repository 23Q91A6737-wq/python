# property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit : we can Add additional logic when read , write , or delete attributes
#             Gives you getter , setter and deleter method


class Rectangle:

    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property

    def width(self):
        return f"{self._width:.2f}cm "

    @property

    def height(self):
        return f"{self._height:.4f}cm"

    @width.setter

    def width(self,new_width):
        if new_width >0:
            self._width = new_width
        else:
            print(f"the new width must be > 0")

    @height.setter

    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("the new height must be greater than 0")

    @width.deleter

    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter

    def height(self):
        del self._height
        print("the height has been deleted")

rectangle = Rectangle(3,4)


rectangle.width = 7   # it is setter method used to overwrite the method as we set the width 3 to 7 by using @width.setter method

rectangle.height = 8



print(rectangle.width)
print(rectangle.height)


del rectangle.width
del rectangle.height

#Part	                             Job
#width	                         stores the real value
#@property (getter)	             Controls how it is shown/returned
#@setter	                     Controls how it is changed