# FUNCTIONS & RECURSIONS

# 1. Write a program using functions to find greatest of three numbers.
# def greatest_num(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=c and b>=a:
#         return b
#     else:return c
    #### or
    #  return max(n,m,o)

# n=int(input("Enter numbers: "))
# m=int(input("Enter numbers: "))
# o=int(input("Enter numbers: "))
# print(f"The greatest number is {greatest_num(n,m,o)}")


# 2. Write a python program using function to convert Celsius to Fahrenheit.
# def c_to_f(c):
#    f = (c/5)*9+32
#    return f

# def f_to_c(f):
#    c = (f - 32) * 5 / 9
#    return c

# c = int(input("Enter a tempreature in C: "))
# f = int(input("Enter a tempreature in f: "))

# print(f"The temperature in F is {round(f_to_c(f),2)}°C ")
# print(f"The temperature in F is {c_to_f(c)}°F ")


# 3. How do you prevent a python print() function to print a new line at the end
# 4. Write a recursive function to calculate the sum of first n natural numbers.
# n = int(input("Enter a number:"))
# def sum_num(n): 
#   if n==1:
#     return 1
#   elif n<0:
#     return "Invalid input"
#   else :
#    a =  n +sum_num(n-1)
#   return a
# print(f"The sum of the first natural numbers is {sum_num(n)}")


# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
#  *   
# def pattern(n):
#     for i in range(1, n+1):
#         print("*"*((n+1)-i))
# n = int(input("Enter a number: "))
# pattern(n)


# 6. Write a python function which converts inches to cms.
# Centimeters = Inches × 2.54
# i = float(input("Enter number of inches: "))
# def i_to_cm(i):
#     cm =i*2.54
#     return cm
# print(f"The value of inches in cm is {i_to_cm(i)} cm")

# 7. Write a python function to remove a given word from a list and strip it at the same time.
# list = ["apple", "mango", "Banana", "guava", "grapes"]
# def strip_word(lst, word):
#     word = word.strip()  # Ensure the input word is stripped
#     return [item for item in lst if item.strip() != word]  # Filter out the word

# word = input("Enter a word you want to remove: ")
# a = strip_word(list, word)
# print(a)

# b = "neha"
# print(b.strip("a"))
# 8. Write a python function to print multiplication table of a given number.
def multiplication(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
   

n = int(input("Enter a number: "))    
multiplication(n)