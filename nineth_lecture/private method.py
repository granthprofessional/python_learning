class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()      # allowed inside class

p1 = Person()
p1.welcome()
# p1.__hello()   # ERROR