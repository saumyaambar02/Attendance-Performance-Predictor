# marks.py
import csv
import os
from student import student_record

marksheet = "marks.csv"

def add_marks():
    if not os.path.isfile(student_record):
        print("Add students first.\n")
        return

    test_name = input("Enter exam/test name: ")

    stud = []
    with open(student_record, "r") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            stud.append(row)

    entries = []

    for s in stud:
        try:
            score = float(input(f"Marks for {s[1]}: "))
        except:
            score = 0
        entries.append([s[0], s[1], test_name, score])

    if not os.path.isfile(marksheet):
        with open(marksheet, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["RollNo", "Name", "Test", "Marks"])

    with open(marksheet, "a", newline="") as f:
        w = csv.writer(f)
        w.writerows(entries)

    print("\nMarks saved!\n")