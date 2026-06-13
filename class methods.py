#      class methods

# Class methods = Allow operations related to class itself
#                  Take (cls) as the first parameter ,  which represents the class itself.


class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f" {self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f" Total no.of students {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count== 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"

student1 = Student("Ben10",7.0)
student2 = Student("Tom and Jerry",10)
student3 = Student("Bey Blade",8.0)


print(Student.get_count())

print(Student.get_average_gpa())

# https://chatgpt.com/share/69971239-1ec4-800e-8935-77f8f5197b13

# more about class you can go to above link