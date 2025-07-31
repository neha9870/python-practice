
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