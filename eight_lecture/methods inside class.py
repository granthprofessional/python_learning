class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def get_average(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "your average score is", total / len(self.marks))

s1 = Student("Karan", [90, 80, 70])
s1.get_average()

s2 = Student("Arjun", [40, 50, 60])
s2.get_average()


#modifying attributes
s1.name = "granth"
s1.get_average()


