

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

spam = ["make a lot of money", "buy now","subscribe this","click this"]
l1 = "Make a lot of money"
l2= "buy now"
l3= "subscribe this"
l4 = "click this"

message = input("Enter your comment:").lower()
if(l1.lower() in message or l2.lower() in message or l3.lower() in message or l4.lower() in message):
    print("This is spam")
else:
    print("This is not spam")

