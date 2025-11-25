# Attendance-Performance-Predictor

# Overview of the Project** 

This project is basically a menu driven Python application that helps manage students, their attendance, marks, and even predicts if a student is at risk of failing. Instead of manually checking everything, the system automates the whole process and gives simple reports and a basic prediction using ML. I made it in a modular way so each part of the system is separate and easy to understand. 


## 🎯 Features

### 1.⁠ ⁠Student Management

Add new students with their names and roll numbers

View the complete list of registered students

Data stored in students.csv


### 2.⁠ ⁠Attendance Tracking

Mark attendance (P/A) for every student on any given date

View attendance record in a summarized format

Data stored in attendance.csv


### 3.⁠ ⁠Marks Recording

Add marks for any exam/test

Stores marks for each student along with test name

Data stored in marks.csv


### 4.⁠ ⁠Reports & Summary

Attendance percentage for each student

Pie chart visualization of present vs. absent

Marks summary for every student across tests


### 5.⁠ ⁠Risk Prediction (Machine Learning)

Uses a simple Logistic Regression model to identify students who may be:

At Risk

Safe

The model considers:

Attendance Percentage

Average Marks


A student is flagged “At Risk” if either:

Attendance < 75%

Marks < 40


This makes the system helpful for early academic intervention.


---

🧠 How the System Works

The system is modular, with each function kept in a separate file:

File	Responsibility

student.py	Add and view students
attendance.py	Mark and display attendance
marks.py	Enter marks for tests
report.py	Attendance & marks summaries + charts
predictor.py	Machine-learning based risk prediction
main.py	Menu-driven interface that links everything together


Each module uses CSV storage, keeping the project simple and portable.


---

📂 Project Structure

📁 Project Folder
│
├── main.py
├── student.py
├── attendance.py
├── marks.py
├── report.py
├── predictor.py
│
├── students.csv        
├── attendance.csv      
└── marks.csv           


---  

## Tools Used

- Python 
- Pandas
- Matplotlib 
- Scikit-learn 
- CSV files for storing all the data 


## Steps to Install and Run the Project
  
1. Make sure Python is installed.
    
2. Install required libraries by running: 
pip install pandas matplotlib scikit-learn 

3. Keep all Python files (modules) in the same folder.
    
4. Run the project using: 
python main.py  

5.⁠ ⁠Choose options from the menu:

1. Add Student
2. Mark Attendance
3. Add Marks
4. Attendance Report
5. Marks Report
6. Predict Risk
7. View Students
0. Exit

---

🧪 Example Workflow

1.⁠ ⁠Add students


2.⁠ ⁠Mark their attendance for several days


3.⁠ ⁠Enter marks for at least one test


4.⁠ ⁠View attendance summary


5.⁠ ⁠View marks summary


6.⁠ ⁠Run risk prediction


7. View student

The prediction works best when there is enough attendance & marks data.


---

📊 Risk Prediction Logic (Simplified)

The project uses Logistic Regression to classify students into:

“Safe”

“At Risk”


Based on:

Attendance %

Average Marks


This makes the system more than just a record-keeping tool—
it provides actionable insights that can help identify struggling students early.


---

🌟 Why This Project Is Useful

- Helps automate basic student management

- Gives teachers/admins a quick overview of performance

- Supports early detection of low-performing students

- Easy to extend (databases, GUI, dashboards, etc.)



---

## 📌 Future Improvements:

- Add a database (MySQL / SQLite)

- Build a GUI using Tkinter or a web app using Flask

- Add more ML models for better prediction

- Export reports as PDF

- Add student search/update/delete features


## Instructions for Testing

- First add at least one or two students. 

- Then mark attendance for them (P or A). 

- Add marks for any exam. 

- After entering some data, try the reports option to see if things look fine. 

- Finally, use the “Predict Risk” option and check if the model gives sensible output. 
