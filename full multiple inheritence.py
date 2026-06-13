# Full program   -> since all food cycle comes under Animal Habitat


class Animal:

    def __init__(self,name):

        self.name = name

    def sleep(self):
        print(f"The {self.name} is sleeping")

    def eat(self):
        print(f"this {self.name} is eatng")



class Prey(Animal):

    def flee(self):
        print(f" {self.name} is fleeing ")

class Predator(Animal):

    def hunt(self):
        print(f"this {self.name} is hunting ")



class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Mickey")

hawk = Hawk("Tony")

fish = Fish("Nemo")



rabbit.flee()
rabbit.eat()
hawk.hunt()     # if hawk.flee -> the output will show -------> "'Hawk' object has no attribute 'flee'"   since it is only have attribute ----------> "hunt" and this case will apply same to rabbit.hunt

print()

fish.flee()    # since it is multiple inheritence it can apply both hunt and flee because it has two attributes prey and predator
fish.hunt()
