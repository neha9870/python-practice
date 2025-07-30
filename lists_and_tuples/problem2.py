
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