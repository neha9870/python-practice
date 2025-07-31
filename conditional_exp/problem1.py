# 1. Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter a number:"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
d = int(input("Enter a number"))
if(a>b and a>c and a>d):
    print(f"{a} is greatest number")
elif(b > c and b>d and b>a):
    print(f"{b} is greatest number")
elif(c>d and c>a and c>b):
    print(f"{c} is greatest number")
else:
    print(f"{d} is greatest number")
