
# 3. Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    salary = 80000
    increment= 20/100

    @property
    def salaryAfterIncrement(self):
     return f"Increment: {self.increment}\nSalary After Increment is {self.salary}"

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.salary = salary + (salary*Employee.increment)
        self.increment = self.salary - salary


e = Employee()
e.salaryAfterIncrement = Employee.salary
print(e.salaryAfterIncrement)