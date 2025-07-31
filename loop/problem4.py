

######### PROBLEM 4.  Write a program to find whether a given number is prime or not.
number = int(input("Enter a number"))
for i in range(0,number):
    if(number%2==0):
        print("This is not a prime number")
    else:print("This is a prime number")
