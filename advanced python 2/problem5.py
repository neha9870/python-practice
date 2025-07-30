from functools import reduce

# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
l = [ 3, 56, 23, 78, 89, 23, 100, 34, 27, 68, 343, 10]
def maximum(a,b):
    if a>b : return a
    else: return b
result = reduce(maximum, l)
print(result)    