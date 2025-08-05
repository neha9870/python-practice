import random
# 
# 
# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
# class Programmar():
    
#     name = "Rohan"
#     salary = "1000000"
#     language = "Python"
#     age = 34
#     print(f"Name: {name} \nSalary: {salary}\nLanguage: {language}\nAge: {age}")
# rohan = Programmar()    

# or###
# class Programmer():
#     def __init__(self, name, salary, age, language):
#         self.name = name
#         self.salary = salary
#         self.language = language
#         self.age = age


# rohan = Programmer("Rohan", 1200000, 34, "Python")
# print(rohan.name, rohan.salary, rohan.age, rohan.language)        

# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.

# class Calculator():
#     def __init__(self,n):
#         square = n**2
#         print(f"The Square of {n} is {square}")
#         cube = n**3
#         print(f"The Cube of {n} is {cube}")
#         square_root = n**1/2
#         print(f"The Square Root of {n} is {square_root} ")
# n = int(input("Enter a number: "))
# num= Calculator(n)   


# 3. Create a class with a class attribute a; create an object from it and set ‘a’/
# directly using ‘object.a = 0’. Does this change the class attribute?  # Noooo
# class demo():
#     a = 23
# object = demo()
# print(object.a) # prints class attributes because instance attribute is not present
# object.a = 0
# print(object.a) # prints class attributes because instance attribute is  present
# print(demo.a)   # prints class attributes

# 4. Add a static method in problem 2, to greet the user with hello.

# class Calculator():
#     def __init__(self,n):
#         square = n**2
#         print(f"The Square of {n} is {square}")
#         cube = n**3
#         print(f"The Cube of {n} is {cube}")
#         # square_root = n**0.5
#         square_root = n**(1/2)
#         print(f"The Square Root of {n} is {square_root} ")
#     @staticmethod
#     def greet():
#        print("Hello Python Learner")


# n = int(input("Enter a number: "))
# num= Calculator(n)   
# num.greet()
 
# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways. 
# class train():
#     def __init__(self, name, age, gender, train_no, fro, to):
#         print(f"Train is booked from {fro} to {to}.\nTrain no. :{train_no}")
#         print(f"Name of passenger: {name}\nAge: {age}\nGender: {gender}\n")

# train_no = random.randint(10000,99999)
# name = input("Enter your name: ").capitalize()
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ").capitalize()
# fro = input("Enter from:").capitalize()
# to = input("Enter to:").capitalize()

# neha = train(name, age, gender, train_no, fro, to)


# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# # vector.
# class twodvector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
      
#     def show(self):
#           return f"The vector of point({self.x},{self.y}) is {self.x}i + {self.y}j"       
#     # def __str__(self):
#     #     return f"The vector of point({self.x},{self.y}) is {self.x}i + {self.y}j"    

# class threedvector(twodvector):
#     def __init__(self,x,y,z):
#      super().__init__(x,y)
#      self.z = z

#     # def __str__(self):
#     #    return f"The vector of point({self.x},{self.y},{self.z}) is {self.x}i + {self.y}j + {self.z}k"    
#     def show(self):return  f"The vector of point({self.x},{self.y},{self.z}) is {self.x}i + {self.y}j + {self.z}k"   
 


# n=twodvector(1,2)
# m=threedvector(4,5,6)  
# print(n.show())
# # n.show()
# # m.show()
# print(m.show())  

# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
# class Animals:
#     pass

# class Pets (Animals):
#     pass
# class Dog(Pets):
#     def bark(self):
#         print("dogs bark")    


# a = Animals()
# p = Pets()
# d = Dog()
# d.bark()


# 