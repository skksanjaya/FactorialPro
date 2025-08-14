class Employee:
    def __init__(self,name,salary,job_title):
        self.details=[name,salary,job_title]

    def display_info(self):
        print(f"Name: {self.details[0]}, salary: {self.details[1]}, job_title: {self.details[2]}")

    def give_raise(self,increase):
        self.details[1]=int(self.details[1])+int(increase)


def main():
    name=input("Enter your Name: ")
    salary=input("Enter your Salary: ")
    title=input("Enter your Title: ")
    p1=Employee(name,salary,title)
    name=input("Enter your Name: ")
    salary=input("Enter your Salary: ")
    title=input("Enter your Title: ")
    p2=Employee(name,salary,title)
    p1.display_info()
    p2.display_info()
    raise_sal=input("Enter increase amount: ")
    p1.give_raise(raise_sal)
    p2.give_raise(raise_sal)
    p1.display_info()
    p2.display_info()

if __name__=="__main__":
    main()
