class Person:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age
class Student(Person):
    def __init__(self,acdemicRecord):
        self.acdemicRecord=acdemicRecord

class Staff(Person):
    def __init__(self,taxCode):
        self.taxCode=taxCode

class Academic(Staff):
    def __init__(self,salary):
        self.salary=salary

class General(Staff):
    def __init__(self,payRate):
        self.payRate=payRate                

    
     
