
########### PROBLEM 1. Write a program to print multiplication table of a given number using for loop
number = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")
number = int(input("Enter a number:"))
i=0
########## PROBLEM 2 using while loop.
while(i<=10):
    print(f"{number} X {i} = {number*i}")
    i += 1


########## PROBLEM 3. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if("S" in i ):
        print("Hello ",i)
    else:pass

# ##### or 
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print("Hello", name)

######### PROBLEM 4.  Write a program to find whether a given number is prime or not.
number = int(input("Enter a number"))
for i in range(0,number):
    if(number%2==0):
        print("This is not a prime number")
    else:print("This is a prime number")

 ######## PROBLEM 5.  Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter a number: "))
i = 1
sum = 0
while (i<=n):
    # sum += i
    sum=sum+i
    i += 1   
print(sum) 


######## PROBLEM 6. Write a program to calculate the factorial of a given number using for loop.
n=int(input("Enter a number: "))
product=1
for i in range(1,n+1):
    product=product*i
print(f"The factorial of {n} is {product}")
##### or
# n = int(input("Enter a number: "))
# factorial = n*(n-1)
# print("factorial")


######## PROBLEM 7. Write a program to print the following star pattern.
# *
# ***
# # ***** for n = 3
n=input("Enter a number: ")
product= "*"
i=0
for i in n:
    product=product*i
print(product)   


######## PROBLEM 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="")
    print("")
for i in range(1,n+1):
    print("*"*i, end="")
    print("")


####### PROBLEM 9 Write a program to print the following star pattern.
# * * *
# *   *    for n = 3
# * * *
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2), end="")
        print("*")


######## PROBLEM 10 Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")

       
