class personDetail:
    def __init__(self,name: str,age: int,address: str):
        self.details=[name,age,address]

    def get_data(self,i: int):
        return self.details[i]
    
    def update_age(self,add_age: int):
        self.details[1]=int(self.details[1])+int(add_age)
        return self.details[1]
    
def main():
    name=input("Enter your Name: ")
    age=input("Enter your Age: ")
    address=input("Enter your Address: ")
    p1=personDetail(name,age,address)
    print(f"Name: {p1.get_data(0)}")
    print(f"Age: {p1.get_data(1)}")
    print(f"Address: {p1.get_data(2)}")
    years=input("Enter to add years: ")
    print(f"New Age: {p1.update_age(years)}")


    
if __name__ == "__main__":
        main()
