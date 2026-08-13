class Car:
    color = "black"

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):        # inherits Car
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.name)
print(car1.color)
car1.start()
car1.stop() 


#multi level inheritance(super)
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        super().__init__("Toyota")   # parent constructor call

car1 = Fortuner("diesel")
print(car1.type)
print(car1.brand)
car1.start()






#multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)