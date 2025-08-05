# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return f"{self.x + other.x}i + {self.y + other.y}j + {self.z + other.z}k"

    def __mul__(self,other):
            return f"{self.x*other.x + self.y*other.y + self.z*other.z}"


v1 = Vector(1,2,3)
v2  = Vector(4,5,6)
v3 =v1 + v2
v4 = v1*v2
print(v3)
print(v4)            

########## or 
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = v1 + v2   # Returns a Vector object
v4 = v1 * v2   # Returns a number (dot product)

print(v3)  # 5i + 7j + 9k
print(v4)  # 32
