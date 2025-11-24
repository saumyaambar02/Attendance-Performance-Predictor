# attendance.py
import csv
import os
from student import student_record

attendance_record = "attendance.csv"

def mark_attendance():
    if not os.path.isfile(student_record):
        print("Add students first.\n")
        return

    todays_date = input("Enter date (YYYY-MM-DD): ")

    # Student list
    students = []
    with open(student_record, "r") as f:
        r = csv.reader(f)
        next(r, None)
        for s in r:
            students.append(s)

    entries = []
    print("\nMark P for present and A for absent:\n")

    for stu in students:
        att = input(f"{stu[1]}: ").strip().upper()
        if att not in ["P", "A"]:
            att = "A"
        entries.append([stu[0], stu[1], todays_date, att])

    # Create file if missing
    if not os.path.isfile(attendance_record):
        with open(attendance_record, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["RollNo", "Name", "Date", "Attendance"])

    with open(attendance_record, "a", newline="") as f:
        w = csv.writer(f)
        w.writerows(entries)

    print("\nAttendance saved!\n")


def show_attendance():
    if not os.path.isfile(attendance_record):
        print("No attendance data found.\n")
        return

    with open(attendance_record, "r") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            print(f"{row[2]} - {row[1]}: {row[3]}")