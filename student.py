# student.py
import csv
import os

student_record = "students.csv"

def add_student():
    student_name = input("Student Name: ").strip()
    roll_no = input("Roll Number: ").strip()

    file_exists = os.path.isfile(student_record)

    # Create file if missing
    if not file_exists:
        with open(student_record, "w", newline="") as f:
            write = csv.writer(f)
            write.writerow(["RollNo", "Name"])

    # Add details
    with open(student_record, "a", newline="") as f:
        write = csv.writer(f)
        write.writerow([roll_no, student_name])

    print("Student added!\n")


def view_students():
    if not os.path.isfile(student_record):
        print("No student data available.\n")
        return

    with open(student_record, "r") as f:
        read = csv.reader(f)
        next(read, None)
        for row in read:
            print(f"{row[0]} - {row[1]}")