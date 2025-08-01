# ############### OOPS
class Employee:

  @property
  def name(self):
    # return self.ename
    #   return self.lname
    #   return self.fname
      return f"{self.fname} {self.lname}"

  @name.setter
  def name (self,value):
    # self.ename = value
    self.fname = value.split(" ")[0]
    self.lname = value.split(" ")[1]


e=Employee()
e.name = "Rohan Verma"    
# print(e.fname, e.lname)
print( e.name)
# print(e.fname)
# print(e.lname)

