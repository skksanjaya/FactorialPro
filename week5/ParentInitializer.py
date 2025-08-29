class Person:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age

    def greet(self):
        print("Greetings : "+self.name)  

class Student(Person):
    def __init__(self,name,address,age,studentID):
        super().__init__(name,address,age) 
        self.studentID=studentID

    def greet(self):
        print("Greetings : "+self.name +self.address)  
        super().greet()  

class Staff(Person):
    def __init__(self,taxCode):
        self.taxCode=taxCode

class Academic(Staff):
    def __init__(self,salary):
        self.salary=salary

class General(Staff):
    def __init__(self,payRate):
        self.payRate=payRate 

def main():
    student1=Student("Nimal","Quenn street",25,"S0001")  
    student1.greet()

if __name__ == "__main__":
    main()
    
     
