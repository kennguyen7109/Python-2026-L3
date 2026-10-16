import numpy as np
import pandas as pd

students_df = pd.read_csv("students.csv")
scores_df = pd.read_csv("scores.csv") #load both
print("Missing values in students.csv: ")
print(students_df.isna().sum()) #check missing in stu
print("Missing values in scorse.csv: ")
print(scores_df.isna().sum()) #check missing in scores
students_df["age"] = students_df["age"].fillna(students_df["age"].median()) #fill age in stu
students_df["GPA"] = students_df["GPA"].fillna(students_df["GPA"].mean()) #fill gpa in stu
scores_df["math"] = scores_df["math"].fillna(scores_df["math"].mean()) #fill math in scores
scores_df["database"] = scores_df["database"].fillna(scores_df["database"].mean()) #fill data in scores
merge = pd.merge(students_df, scores_df, on="student_id") #merge
print(merge.head()) #display merge
merge["avr"] = merge[["python", "math", "database"]].mean() #avr 
print(merge[["python","math","database"]].head()) #display avr
top5 = merge.sort_values(by="avr",ascending=False)
print(f"Top 5 students: {top5[["student_id","name","age","avr"]]}")
avr_major = merge.groupby("major")["avr"].mean()
print(avr_major)