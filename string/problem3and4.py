
# 3. Write a program to detect double space in a string.


# 4. Replace the double space from problem 3 with single spaces.
a = "Welcome to Python!  Python is a high level programming"
print(a.find("  "))
print(len(a))
print(a.replace("  ", " "))
print(a)   #Strings are immutable which means that you cannot change them by running functions on them
