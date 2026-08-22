class Complex: 
#BE SELFISH FOR YOUR SELF !! 
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

    def __sub__(self, num2):
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)


n1 = Complex(1, 3)
n2 = Complex(4, 6)
n1.show_number()
n2.show_number()

n3 = n1 + n2
n3.show_number()

n4 = n1 - n2
n4.show_number()