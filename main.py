# main.py
from student import add_student, view_students
from attendance import mark_attendance, show_attendance
from marks import add_marks
from report import attendance_summary, marks_summary
from predictor import risk_prediction

def Menu():
    while True:
        print(" Attendance System ")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Add Marks")
        print("4. Attendance Report")
        print("5. Marks Report")
        print("6. Predict Risk")
        print("7. View Students")
        print("0. Exit\n")

        option = input("Select option: ").strip()

        if option == "1":
            add_student()
        elif option == "2":
            mark_attendance()
        elif option == "3":
            add_marks()
        elif option == "4":
            attendance_summary()
        elif option == "5":
            marks_summary()
        elif option == "6":
            risk_prediction()
        elif option == "7":
            view_students()
        elif option == "0":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    Menu()