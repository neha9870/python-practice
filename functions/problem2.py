
# 2. Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f(c):
   f = (c/5)*9+32
   return f

def f_to_c(f):
   c = (f - 32) * 5 / 9
   return c

c = int(input("Enter a tempreature in C: "))
f = int(input("Enter a tempreature in f: "))

print(f"The temperature in F is {round(f_to_c(f),2)}°C ")
print(f"The temperature in F is {c_to_f(c)}°F ")
