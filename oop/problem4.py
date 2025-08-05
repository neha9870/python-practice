# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

####### Without __str__
class Complex:
    def __init__(self,r,i):
        self.r =r
        self.i = i

    def __add__(self,other):
        return f"{self.r + other.r} + {self.i + other.i}i"

    def __mul__(self,other):
        real = self.r*other.r - self.i*other.i
        img = self.i*other.r + self.r*other.i
        return f"{real} + {img}"

v1 = Complex(2,4)
v2 = Complex(3,5)
v3 = v1+v2
v4 = v1*v2
print(v3)
print(v4)



     #########  With __str__

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        real = self.r*other.r - self.i*other.i
        img = self.r*other.i + self.i*other.r
        return Complex(real, img)

    def __str__(self):
        return f"{self.r} + {self.i}i"


    

v1 = Complex(2, 4)
v2 = Complex(3, 5)
v3 = v1 + v2
v4 = v1*v2
print(v3) 
print(v4) # Now this prints: 5 + 9i


