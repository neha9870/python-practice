

# 5. Write a program which finds out whether a given name is present in a list or not.

list = ["Neha", "Sunita", "Amit", "Rohan", "Dhruv", "Tushar", "Geeta", "Shivani", "Vedika", "Vidya"]
name = input("Enter your name: ").capitalize()
if(name in list):
    print("Your name is present in list.\nSo, you are selected")
else:print("Your name is not present in list.\nSo, you are not selected.")

