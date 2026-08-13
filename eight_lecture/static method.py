class Student:
    @staticmethod
    def hello():
        print("hello")

s1 = Student()
s1.hello()


#abrstracrtion(car start expample)
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()



#encpsulation
'''# concept: data (attributes) + related functions (methods)
# wrapped inside one class = capsule
# har class jo humne banayi upar, wahi encapsulation hai'''