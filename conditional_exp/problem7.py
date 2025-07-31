
# 7. Write a program to find out whether a given post is talking about “Harry” or not.
n = "Neha" 
post = input("Enter your post:")
if (n.lower() in post or n in post or n.upper() in post):print("This post talking about Neha")
else:print("This post not talking about Neha")

#######or 


post = input("Enter your post:")
if("Neha".lower() in post.lower()):print("This post talking about Neha")
else:print("This post not talking about Neha")

