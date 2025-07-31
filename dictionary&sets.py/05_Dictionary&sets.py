# DICTIONARY & SETS

########## dictionary   ########################

a = { 
    "key":"value",
    "list":[1,2,3,5,7,5,3,56,7],
    "Neha":89,
    "Shubham":67,
    "Geeta":93,
    "Shikha":50,
}

print(a, type(a))
print(a["Geeta"])
print(a['key'])
print(a["list"])
print(a.items())
print(a.keys())
print(a.values())
a.update({"Neha":97})
a.update({"Ran":53})
print(a.get("Neha"))
a.get("Neha")
print(a.get("Neha2")) 
#prints None
print(a["Neha2"]) #prints an error
a.clear()
a.copy() 
print(a)


########### sets in python    ####################
s = set()  # not allowed repitition
print(type(s))
s.add(1)
print(s)
s.add(2)
print(s)
s.add(3)
print(s)

b = {1,2,3,4}
c = {14,15,27,1}

e = set() # dont use s = {} as it will create an empty dictionary
q={}
print(q,type(q))
print(type(e))
print(b , type(b))

##### operations on sets 
print(len(b))
b.remove(3)
b.pop()
b.pop()########### set ke aage se pop hota h
print(b.union(c))
print(b.intersection(c))
print(b.difference(c))
print(c.difference(b))
print({2,3}.issubset(b))
print(b.issuperset({2,3}))
print({2,3}.issubset(c))
b.pop()
print(b)


print(type(b), type(c))

#########3 if elife else ladder

a = int(input("Enter your age:"))
if(a>=18):
    print("You are above of the consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:print("You are below thw age of consent")
print("End of program")


a = 20
b = 20.0
c = 20.1
if(a==b):
    print("you are right")
else: print("not correct")

if (a==c):
    print("yes Neha")
else: print("nooooooooooo")


set = {2,34,4,3,2,53,3,3,4,3,4}
set.remove(3)
print(set)




# ############### DICTIONARY & SETS PRACTICE PROBLEMS ####################





# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

d = {"padhna":"read", "bolna": "speak", "hasna":"laugh","chalna":"walk"}
e = input("Do you want to show meanings of hindi words in English.\nYes or No:")
# if e.capitalize() == "Yes":
if (e.capitalize() == "Yes"):

     print(d)
else: 
    print("Okay, Meanings will not be shown")

#     ############# or ####################

word = input("Enter your word you want meaning of:")
print(d[word])

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).


numbers = set()
print(type(numbers))
n1 = input("Enter any 1st number:")
numbers.add(n1)
n2 = input("Enter any 2nd number:")
numbers.add(n2)
n3 = input("Enter any 3rd number:")
numbers.add(n3)
n4 = input("Enter any 4th number:")
numbers.add(n4)
n5 = input("Enter any 5th number:")
numbers.add(n5)
n6 = input("Enter any 6th number:")
numbers.add(n6)
n7 = input("Enter any 7th number:")
numbers.add(n7)
n8 = input("Enter any 8th number:")
numbers.add(n8)
print(numbers)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
t = set()
t.add(18)  ######### as a int value
t.add("18")  ########### as a string value
print(t)

# 4. What will be the length of following set s:
k = set()
k.add(20)
k.add(20.0)
k.add("20")
print(k,len(k))





# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

friends = {}
name = input("Enter your name:")
language= input("Enter your favorite language:")
friends.update({name.capitalize():language.capitalize()})
name = input("Enter your name:")
language= input("Enter your favorite language:")
friends.update({name.capitalize():language.capitalize()})
name = input("Enter your name:")
language= input("Enter your favorite language:")
friends.update({name.capitalize():language.capitalize()})
name = input("Enter your name:")
language= input("Enter your favorite language:")
friends.update({name.capitalize():language.capitalize()})

print(friends)

# 8. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
s = {8,7,12,"Harry",(1,2)}
print(s)

