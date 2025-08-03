########## File I/O  ##########
import random
# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
# f = open("poems.txt")
# content = f.read()
# if ("twinkle" in content):
#     print("The word 'twinkle' is present in the file.")
# else:
#     print("The word 'twinkle' is not present in the file.")         
# f.close()
# or using 'with' statement##########

# with open("file_io/poems.txt") as f:
#     content = f.read()
#     if "twinkle" in content:
#         print("The word 'twinkle' is present in the file.")
#     else:
#         print("The word 'twinkle' is not present in the file.")
# 
#  
# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score.
# # 
# def game(score):
#     with open("file_io/game._score.txt") as f:
#         high_score = f.read()
#         if high_score != "":
#            high_score = int(high_score)
#         else:
#             high_score = 0
    
#         if score>high_score:
#             with open("file_io/game._score.txt", "w") as f:
#                  f.write(str(score))
#             print(f"New High Score: {score}") 
#             return score
#         else:print(f"Your score:{score}, High Score: {high_score}")
#         return high_score    


# score = random.randint(1,100)
# your_score = game(score)

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
#  different files. Place these files in a folder for a 13 – year old.

# def table(n):
#     with open(f"file_io/table_{n}.txt","w") as f:
#         for i in range(1,11):
#            f.write(f"{n} X {i} = {n*i}\n")


# for n in range(2,21):
#     table(n)


# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.
   
# with open("file_io/01_file.txt", "r") as f:
#     content = f.read()
#     word = "Donkey"

# if word in content:
#    with open("file_io/01_file.txt", "w") as f:
#         new_content = content.replace(word, "#####")
#         f.write(new_content)
#         print("found")
# else:print("not found")

# 5. Repeat program 4 for a list of such words to be censored.
# with open("file_io/01_file.txt","r") as f:
#     content = f.read()
# words =["Donkey", "human", "helps", "hardworking"]
# for word in words:  
#     content = content.replace(word, "#######") 
# with open("file_io/01_file.txt", "w") as f:
#     f.write(content)

# 6. Write a program to mine a log file and find out whether it contains ‘python’.
# with open("file_io/02_file.txt", "r") as f:
#     content = f.read()
# if "Python" in content:
#         print("Python word is present")
# else:print("Python word is not present")

# 7. Write a program to find out the line number where python is present from ques 6.
lineno = 1
found = False
with open("file_io/02_file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if "Python" in line:
           print(f"Python word is present in this line no. {lineno}") 
           found = True
        lineno = lineno + 1   
    if not found:print("not present")
   
        #    print("not present")
      