import pandas as pd
a = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Simran", "Karan"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT", "CSE", "ECE"],
    "City": ["Lucknow", "Delhi", "Lucknow", "Kanpur", "Delhi", "Noida", "Kanpur"],
    "Attendance": [90, 75, 85, 60, 95, 80, 70]
})

b = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105, 106, 108, 109],
    "Python": [88, 65, 92, 78, 85, 70, 60],
    "SQL": [80, 72, 95, 82, 79, 75, 55],
    "Project": [90, 60, 96, 85, 88, 72, 58]
})
c=a.merge(b)
print(c)

