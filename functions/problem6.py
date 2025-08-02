
# 6. Write a python function which converts inches to cms.
# Centimeters = Inches × 2.54
i = float(input("Enter number of inches: "))
def i_to_cm(i):
    cm =i*2.54
    return cm
print(f"The value of inches in cm is {i_to_cm(i)} cm")

