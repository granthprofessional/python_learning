#basic class + object
'''class Student:
    name = "Karan"

s1 = Student()
print(s1)
print(s1.name)

s2 = Student()
print(s2.name)'''

#car class(class level attributes)
class Car:
    color = "blue"
    brand = "Mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)


#constructor(int)
class Student:
    def __init__(self):
        print("adding new student in database")
        self.name = "anonymous"

s1 = Student()
print(s1.name)