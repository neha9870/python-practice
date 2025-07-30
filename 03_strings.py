print("Hello Python")

# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name:").capitalize
print("Good Afternoon", name)


# 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Neha").replace("<|Date|>", "21 January 2070"))


# 3. Write a program to detect double space in a string.


# 4. Replace the double space from problem 3 with single spaces.
a = "Welcome to Python!  Python is a high level programming"
print(a.find("  "))
print(len(a))
print(a.replace("  ", " "))
print(a)   #Strings are immutable which means that you cannot change them by running functions on them


# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, this python course is nice. Thanks!"
letter = "Dear Neha,\n\tThis python couse is nice.\nThanks!"
name = "Vedika"
print(letter)
print(f"Dear {name}, \n\t\t\t\t\tThis python is nice. \nThanks!")















