from com.savvion.sbm.util.config import AbstractConfig
class Employee:

    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.email=fname+'.'+lname+'@aurea.com'
        self.pay=pay


emp_2 = Employee("Test","User","10000")

#print(emp_1.email)
print(emp_2.email)

class MakeUseOfEmployee:

    def __init__(self, emp):
        self.emp=emp
    def getEmpDetails(self):
         return "Name: {0}, age: {1}".format(emp.fname+emp.lname, emp.pay)
        
emp = Employee("Vikas","Pandey","10000")
reusestuff=MakeUseOfEmployee(emp)
print(reusestuff.getEmpDetails())
