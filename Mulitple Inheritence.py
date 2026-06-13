
# Multiple Inheritence

# multiple inheritence = insert from more than one parent class
#                        C(A,B)

# multilevel inheritence = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# step 1:.

class Prey:

    def flee(self):
        print(f" this animal is fleeing ")

class Predator:

    def hunt(self):
        print("this animal is hunting ")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()

hawk = Hawk()

fish = Fish()



rabbit.flee()
hawk.hunt()     # if hawk.flee -> the output will show -------> "'Hawk' object has no attribute 'flee'"   since it is only have attribute ----------> "hunt" and this case will apply same to rabbit.hunt

print()

fish.flee()    # since it is multiple inheritence it can apply both hunt and flee because it has two attributes prey and predator
fish.hunt()


