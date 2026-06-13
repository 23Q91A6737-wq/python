 # Inheritence                          # 6:57:37 Bro Code

 # Inheritence = Allows a class to inherit attributes and methods from another class
 #               Helps with code reusability and extensibility
 #               class Child(Parent)


class Animal:

    def __init__(self,name):  # attributes

        self.name = name
        self.is_alive = True

    def eat(self):  #method
        print(f" the {self.name} is eating")

    def sleep(self):
        print(f" the {self.name} is sleeping")

    def playing(self):
        print(f"the {self.name} is playing Cricket")

class Dog(Animal):
    pass

class Cat(Animal):

    def sleep(self):   # if you want any changes in the inheritance you can again add one and wirte the code . if not  want to change you can pass like  ( Dog (Animal )) which will give answers from the parent and don't need to write the code again . it si your wish based on the output you have to want
        print(f"the cat {self.name } did not sleep")

class Mouse(Animal):
    def playing(self):
        print(f" the {self.name} is playing Free-Fire")

dog = Dog("Scooby-doo")

cat = Cat("Tom")

mouse = Mouse("Mickey")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.playing()

print()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.playing()

print()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.playing()