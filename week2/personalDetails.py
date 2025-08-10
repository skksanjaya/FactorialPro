class personDetail:
    def __init__(self,name,age,address):
        self.details=[name,age,address]

    def get_data(self,i):
        return self.details[i]
    
def main():
    name=input("Enter your Name: ")
    age=input("Enter your Age: ")
    address=input("Enter your Address: ")
    p1=personDetail(name,age,address)
    print(f"Name: {p1.get_data(0)}")
    print(f"Age: {p1.get_data(1)}")
    print(f"Address: {p1.get_data(2)}")

    
if __name__ == "__main__":
        main()
