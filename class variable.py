
# class variables

# class variable = shared among all instance of a class

#                  Defined outside the constructer

#                  Allow you to share data among all objects created from that class

# What does instance mean?

# An instance is a real object created from a class.

# Class = blueprint / template 🏗️

# Instance = actual object made from that blueprint 🚗


class Student:

    class_year = 2024

    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students +=1

student1 = Student("ASH",22)
student2  =Student("Enukula",21)
student3 = Student("Sandy",21)
student4 = Student("Henry",17)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")


print(student1.name)
print(student2.age)
print(student3.name)
print(student4.name)

print(Student.class_year)
print(Student.num_students)
