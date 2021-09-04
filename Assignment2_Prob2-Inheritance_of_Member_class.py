#assignment 2 - Problem 2

#implementation of 3 classes viz Member, Employee and Manager
class Member:
    def __init__(self,name,age,pnum,add,sal):
        self.name = name
        self.age  = age
        self.pnum = pnum
        self.add  = add
        self.sal  = sal

    def printSalary(self):
        print(f"Salary of Member {self.name} is {self.sal}")


class Employee(Member):
    def __init__(self,name,age,pnum,add,sal,spec):
        super().__init__(name,age,pnum,add,sal)
        self.spec = spec

    def printSalary(self): #implemented a different method to show method overriding
        print(f"Salary of Employee {self.name} having specialization {self.spec} is {self.sal}")
        


class Manager(Member):
    def __init__(self,name,age,pnum,add,sal,dept):
        super().__init__(name,age,pnum,add,sal)
        self.dept = dept

    def printSalary(self):
        print(f"Salary of Manager {self.name} of department {self.dept} is {self.sal}")


#driver code 
m1 = Member("Priya",30,"8245682456","Mumbai",45000)
m1.printSalary()

e1 = Employee("Riya",24,"8245682456","Mumbai",40000, "Cloud Computation")
e1.printSalary()

mgr1 = Manager("Supriya",41,"8245682456","Mumbai",65000, "Cloud Systems")
mgr1.printSalary()
