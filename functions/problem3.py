
# 3. How do you prevent a python print() function to print a new line at the end
# 4. Write a recursive function to calculate the sum of first n natural numbers.
n = int(input("Enter a number:"))
def sum_num(n): 
  if n==1:
    return 1
  elif n<0:
    return "Invalid input"
  else :
   a =  n +sum_num(n-1)
  return a
print(f"The sum of the first natural numbers is {sum_num(n)}")