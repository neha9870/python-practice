
# 1. Write a program using functions to find greatest of three numbers.
def greatest_num(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:return c
    ### or
    # return max(n,m,o)

n=int(input("Enter numbers: "))
m=int(input("Enter numbers: "))
o=int(input("Enter numbers: "))
print(f"The greatest number is {greatest_num(n,m,o)}")
