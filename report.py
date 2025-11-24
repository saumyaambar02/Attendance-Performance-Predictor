# report.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from attendance import attendance_record
from marks import marksheet

def attendance_summary():
    if not os.path.isfile(attendance_record):
        print("No attendance found.\n")
        return

    data = pd.read_csv(attendance_record)
    names = data["Name"].unique()

    for n in names:
        person = data[data["Name"] == n]
        total = len(person)
        present = (person["Attendance"] == "P").sum()
        percent = (present / total) * 100

        print(f"{n}: {percent:.1f}%")

        # Graph
        plt.figure()
        plt.pie([present, total - present], labels=["Present", "Absent"], autopct="%.1f%%")
        plt.title(f"Attendance - {n}")
        plt.show()


def marks_summary():
    if not os.path.isfile(marksheet):
        print("No marks found.\n")
        return

    data = pd.read_csv(marksheet)
    names = data["Name"].unique()

    for n in names:
        print(f"\nMarks for {n}:")
        print(data[data["Name"] == n][["Test", "Marks"]])