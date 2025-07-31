

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each  subject to pass. Assume 3 subjects and
# take marks as an input from the user.

English = float(input("Enter your marks of English subject :"))
if( English > 100):
    print("Enter a valid marks")
    English = float(input("Enter your marks of English subject :"))


Maths = float(input("Enter your marks of Maths subject :"))
if(Maths > 100):
    print("Enter a valid marks")
    Maths = float(input("Enter your marks of Maths subject :"))

Science = float(input("Enter your marks of Science subject :"))
if(Science > 100):
    print("Enter a valid marks")
    Science = float(input("Enter your marks of Science subject :"))

Total = (English + Maths + Science)/300*100
subject = [English, Maths , Science]

# print(type(subject))
if(Total >= 40 and  English >= 33 and Maths >= 33 and Science >= 33   ):
    print("You are passed.")
else:print("You are failed")

print(f"Marks:\nEnglish:{English}\nMaths:{Maths}\nScience:{Science}")

