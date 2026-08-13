class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database")

s1 = Student("Karan")
s2 = Student("Arjun")
print(s1.name)
print(s2.name)

#class attribute vs instance attribute
class Student:
    college_name = "ABC College"   # class attribute

    def __init__(self, fullname):
        self.name = fullname       # instance attribute

s1 = Student("Karan")
print(s1.name)
print(s1.college_name)
print(Student.college_name)