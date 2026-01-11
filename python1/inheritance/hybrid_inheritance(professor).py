class Person:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name,"\nage:",self.age)

class Employee(Person):
    def __init__(self, name, age,empid=0):
        super().__init__(name, age)
        self.empid=empid
    def display(self):
        super().display()
        print("Employee id : ",self.empid)

class Faculty(Employee):
    def __init__(self, name, age, empid,dept):
        super().__init__(name, age, empid)
        self.dept=dept
    def display(self):
        super().display()
        print("department:",self.dept)

class Researcher:
    def can_do_research(self):
        return f"{self.name} can do the research"

class Professor(Researcher,Faculty):
    def __init__(self, name, age, empid, dept,sub=None):
        super().__init__(name, age, empid, dept)
        self.sub=sub
    def display(self):
        super().display()
        super().can_do_research()
        print("Subject : ",self.sub)
        

p1=Professor('anna',22,23254,'Commerce','Accounting')
p1.display()