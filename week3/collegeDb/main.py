from database import create_table

# Import managers
from student import StudentData #add_student, view_students, delete_student
from classYB import ClassYB #add_class, view_classes, delete_class
from subject import Subject #add_subject, view_subjects, delete_subject
from lecturer import Lecturer #add_lecturer, view_lecturers, delete_lecturer
from studentAttend import StudentAttend #add_student_attendance, view_student_attendance, delete_student_attendance
from lecturerAttend import LecturerAttend #add_lecturer_attendance, view_lecturer_attendance, delete_lecturer_attendance


def menu():
    print("\n==== School Management System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Delete Student")
    print("4. Add Class")
    print("5. View All Classes")
    print("6. Delete Class")
    print("7. Add Subject")
    print("8. View All Subjects")
    print("9. Delete Subject")
    print("10. Add Lecturer")
    print("11. View All Lecturers")
    print("12. Delete Lecturer")
    print("13. Add Student attend to Class")
    print("14. View Student attend to Class")
    print("15. Delete Student attend to Class")
    print("16. Add Lecturer attend to Class")
    print("17. View Lecturer attend to Class")
    print("18. Delete Lecturer attend to Class")
    print("19. Exit")


def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-19): ")
        classyb=ClassYB()
        studentyb=StudentData()
        subjectyb=Subject()
        lectureryb=Lecturer()
        studentAttendyb=StudentAttend()
        lecturerAttendyb=LecturerAttend()

        if choice == '1':
            name = input("Enter student name: ")
            DOB = input("Enter DOB: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            studentyb.add_student(name, DOB, email, phone)
        elif choice == '2':
            students = studentyb.view_students()
            for student in students:
                print(student)
        elif choice == '3':
            student_id = int(input("Enter student ID to delete: "))
            studentyb.delete_student(student_id)


        elif choice == '4':
            class_name = input("Enter class name: ")
            description = input("Enter description: ")
            classyb.add_class(class_name, description)
        elif choice == '5':
            classes = classyb.view_classes()
            for cls in classes:
                print(cls)
        elif choice == '6':
            class_id = int(input("Enter class ID to delete: "))
            classyb.delete_class(class_id)

        elif choice == '7':
            name = input("Enter subject name: ")
            description = input("Enter description: ")
            class_id = int(input("Enter class ID: "))
            subjectyb.add_subject(name, description, class_id)
        elif choice == '8':
            subjects = subjectyb.view_subjects()
            for subject in subjects:
                print(subject)
        elif choice == '9':
            subject_id = int(input("Enter subject ID to delete: "))
            subjectyb.delete_subject(subject_id)

        elif choice == '10':
            name = input("Enter lecturer name: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            subject_id = int(input("Enter subject ID: "))
            lectureryb.add_lecturer(name, dob, email, phone, subject_id)
        elif choice == '11':
            lecturers = lectureryb.view_lecturers()
            for lec in lecturers:
                print(lec)
        elif choice == '12':
            lecturer_id = int(input("Enter lecturer ID to delete: "))
            lectureryb.delete_lecturer(lecturer_id)

        elif choice == '13':
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            studentAttendyb.add_student_attendance(student_id, class_id)
        elif choice == '14':
            records = studentAttendyb.view_student_attendance()
            for r in records:
                print(r)
        elif choice == '15':
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            studentAttendyb.delete_student_attendance(student_id, class_id)


        elif choice == '16':
            class_id = int(input("Enter class ID: "))
            lecturer_id = int(input("Enter lecturer ID: "))
            lecturerAttendyb.add_lecturer_attendance(class_id, lecturer_id)
        elif choice == '17':
            records = lecturerAttendyb.view_lecturer_attendance()
            for r in records:
                print(r)
        elif choice == '18':
            class_id = int(input("Enter class ID: "))
            lecturer_id = int(input("Enter lecturer ID: "))
            lecturerAttendyb.delete_lecturer_attendance(class_id, lecturer_id)


        elif choice == '19':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
