# 2. Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter your name: ").title()
marks = int(input("Enter your marks: "))
phno = int(input("Enter your phone number: "))

print("The name of the student is {0}, his/her marks are {1} and phone number is {2}".format(name, marks, phno))
