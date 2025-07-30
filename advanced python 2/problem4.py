# 4. Write a program to filter a list of numbers which are divisible by 5.
l = [5, 7, 34, 78, 60, 10, 20, 65, 85, 10000000000000, 345, 1, 2,5, 8, 0]

# n = [] or

divisible = lambda x : x%5==0
result = list(filter(divisible,l))
print(result)

    
