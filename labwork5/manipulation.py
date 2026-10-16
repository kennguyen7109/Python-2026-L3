import pandas as pd

students_df = pd.read_csv("students.csv")
print("First five rows of dataset: ")
print(students_df.head()) #display 5 rows
rows, cols = students_df.shape
print(f"\nNumber of rows : {rows}, number of columns: {cols}") #find rows+cols
name_gpa_df = students_df[["name", "GPA"]] #selct name+gpa
print(name_gpa_df.head()) #display 5 name+gpa
high_gpa = students_df[students_df["GPA"] >= 3.5]
print(f"\nHigh gpa students: {len(high_gpa)}") #find numbers of students>=3.5
sort_student = students_df.sort_values(by="GPA", ascending=False) #sort from high-low 
print(f"\nStudents rank by GPA: {sort_student[["student_id", "name", "GPA"]].head()}") 
avr_gpa_major = students_df.groupby("major")["GPA"].mean() #find average gpa by major
print("\nAverage GPA by major: ") 
print(avr_gpa_major)