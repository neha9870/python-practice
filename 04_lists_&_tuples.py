# LISTS AND TUPLES


# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []
f1 = input("Enter name of  fruit1: ")
fruits.append(f1)
f2 = input("Enter name of  fruit2: ")
fruits.append(f2)
f3 = input("Enter name of  fruit3: ")
fruits.append(f3)
f4 = input("Enter name of  fruit4: ")
fruits.append(f4)
f5 = input("Enter name of  fruit5: ")
fruits.append(f5)
f6 = input("Enter name of  fruit6: ")
fruits.append(f6)
f7 = input("Enter name of  fruit7: ")
fruits.append(f7)
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
m1 = int(input("Enter marks of suject 1st:"))
marks.append(m1)
m2 = int(input("Enter marks of suject 2nd:"))
marks.append(m2)
m3 = int(input("Enter marks of suject 3rd:"))
marks.append(m3)
m4 = int(input("Enter marks of suject 4th:"))
marks.append(m4)
m5 = int(input("Enter marks of suject 5th:"))
marks.append(m5)
m6 = int(input("Enter marks of suject 6th:"))
marks.append(m6)
marks.sort()
print(marks)


# 3. Write a program to sum a list with 4 numbers.
numbers = [5 , 5 , 3, 5]
print(sum(numbers))

# 4. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))