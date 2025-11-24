# predictor.py
import pandas as pd
import os
from attendance import attendance_record
from marks import marksheet
from sklearn.linear_model import LogisticRegression

def risk_prediction():
    if not (os.path.isfile(attendance_record) and os.path.isfile(marksheet)):
        print("Not enough data for prediction.\n")
        return

    att = pd.read_csv(attendance_record)
    mrk = pd.read_csv(marksheet)

    # Attendance %
    att_per = att.groupby("Name")["Attendance"].apply(
        lambda x: (x == "P").sum() / len(x) * 100
    ).reset_index()
    att_per.columns = ["Name", "AttendancePercent"]

    # Marks avg
    avg_marks = mrk.groupby("Name")["Marks"].mean().reset_index()
    avg_marks.columns = ["Name", "AvgMarks"]

    # Merge
    final = pd.merge(att_per, avg_marks, on="Name")

    # Risk rule (manual label for training)
    final["Risk"] = ((final["AttendancePercent"] < 75) | (final["AvgMarks"] < 40)).astype(int)

    X = final[["AttendancePercent", "AvgMarks"]]
    y = final["Risk"]

    model = LogisticRegression()
    model.fit(X, y)

    final["Predicted"] = model.predict(X)

    print("\n--- Risk Prediction ---")
    for _, row in final.iterrows():
        status = "At Risk" if row["Predicted"] == 1 else "Safe"
        print(f"{row['Name']} → {status}")