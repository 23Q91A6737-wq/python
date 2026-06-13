# static method                  # 7:34::00     # important to again see the video in brocode for better explanation


# static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general functions

# Instance methods = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data



class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod

    def is_valid_position(job):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]

        return job in valid_positions

print(Employee.is_valid_position("Cook"))  # it is belonged to the group

print(Employee.is_valid_position("Car Racer")) # it does not belongs to the group

print()

emp1 = Employee("Hawk","Manager")
emp2 = Employee("Eagle","Cashier")
emp3 = Employee("Sea Gull","Cook")

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())