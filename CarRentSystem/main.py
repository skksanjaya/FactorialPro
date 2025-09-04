from database import create_table

# Import managers
from Control.UserCont import UserService 


def menu():
    print("\n==== Car Management System ====")
    print("1. New User")
    print("2. Login")
    print("3. Exit")

def menuAdmin():     
    print("1. View Car")
    print("2. Add Car")
    print("3. Update Car")
    print("4. Delete Class")
    print("5. Approve/Reject Booking")
    print("6. Manage Rxtra Charge")
    print("7. Exit")

def menuCutomer():    
    print("1. View Car")
    print("2. Add Booking")
    print("3. Payment for approved booking")
    print("4. Close/ExtraCharge")
    print("5. Exit")


def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-19): ")
        user=UserService()
        
        if choice == '1':
            name = input("Enter Customer name: ")
            address = input("Enter Address: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            password = input("Enter password: ")
            if (user.user_exists(email)):
                print("Email Already Exsists!")
            else:
                user.add_user(name, address, email,"2",password,phone)
            print("Added Successfully!")
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")



        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
