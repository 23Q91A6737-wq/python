# methods

# methods = methods are actions that objects can perform

class Car:

    def __init__(self,model,year,color,for_sale):

        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

# methods

    def drive(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

    def drive1(self):
        print(f"you drive the {car1.model}")

    def drove(self):
        print(f" you drive the {self.color} {self.model}")

    def describe(self):
        print(f" {self.year} {self.model} {self.for_sale} {self.color}")


car1 = Car("TATA",2017,"Natural Silver",True)
car2 = Car("BMW",1997,"Black",False)
car3 = Car("Mercedes",1987,"Black",True)

print(car1.model)
print()

car2.drive()

car1.drive1()

car2.stop()

car2.drove()

car3.describe()