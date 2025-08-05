# 6.  Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

v1 = vector(7,8,9)
print(v1)            
