import curses
import os
import zipfile
import pickle
from domains import Person, Course, Student
from input import input_courses, input_marks, input_students
from output import list_courses, list_marks, list_students, export_csv, query

base_dir = os.path.dirname(os.path.abspath(__file__))
student_pkl = os.path.join(base_dir, "student.pkl")
course_pkl = os.path.join(base_dir, "course.pkl")
mark_pkl = os.path.join(base_dir, "mark.pkl")
data_file = os.path.join(base_dir, "students.dat")

class StudentManageMentSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
        self.load_data ()
    
    def load_data(self):
        if os.path.exists("data_file"):
            try:
                with zipfile.ZipFile("data_file", "r") as zip_ref:
                    zip_ref.extractall("base_dir")
            except Exception:
                pass
        if os.path.exists("student.pkl"):
            try:
                with open("student.pkl", "rb") as f:
                    self.__students = pickle.load(f)
            except Exception:
                self.__students = []
        if os.path.exists("courses.txt"):
            try:
                with open("course_pkl", "rb") as f:
                    self.__courses = pickle.load(f)
            except Exception:
                self.__courses = []
        if os.path.exists("marks.txt"):
            try:
                with open("mark.pkl", "rb") as f:
                    self.__marks = pickle.load(f)
            except Exception:
                self.__marks = []
    def compress_data(self):
        if self.__students:
            with open("student_pkl", "wb") as f:
                pickle.dump(self.__students, f)
        if self.__courses:
            with open("course_pkl", "wb") as f:
                pickle.dump(self.__courses, f)
        if self.__marks:
            with open("mark_pkl", "wb") as f:
                pickle.dump(self.__marks, f)
        files_compress = [("student.pkl", student_pkl), ("course.pkl", course_pkl), ("mark.pkl", mark_pkl)]
        with zipfile.ZipFile(data_file, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for arcname, filepath in files_compress:
                if os.path.exists(filepath):
                    zip_file.write(filepath, arcname=arcname)       
    def run(self, stdscr):
            curses.curs_set(1) #turn on the entering information
            while True:
                stdscr.clear()
                stdscr.addstr("----Student Management System----")
                stdscr.addstr("\n1. Input Student Information")
                stdscr.addstr("\n2. Input Course Information")
                stdscr.addstr("\n3. Input Marks")
                stdscr.addstr("\n4. List Students (Sorted by GPA)")
                stdscr.addstr("\n5. List Courses")
                stdscr.addstr("\n6. Show Student Marks for each Course")
                stdscr.addstr("\n7. Export data to csv file")
                stdscr.addstr("\n8. Query student data frame")
                stdscr.addstr("\n0. Exit")
                stdscr.addstr("\nEnter your choice (0-8)")
                stdscr.refresh() #update full info to user
                
                choice = stdscr.getkey() 
                if choice == '1':
                    input_students(stdscr, self.__students, Student)
                elif choice == '2':
                    input_courses(stdscr, self.__courses, Course)
                elif choice == '3':
                    input_marks(stdscr, self.__students, self.__courses, self.__marks)
                elif choice == '4':
                    list_students(stdscr, self.__students, self.__courses, self.__marks)
                elif choice == '5':
                    list_courses(stdscr, self.__courses)
                elif choice == '6':
                    list_marks(stdscr, self.__students, self.__courses, self.__marks)
                elif choice == '7':
                    export_csv(stdscr, self.__students, self.__courses, self.__marks)
                elif choice == '8':
                    query(stdscr)
                elif choice == '0':
                    self.compress_data()
                    stdscr.clear()
                    stdscr.addstr("Pickling and compressing data to students.dat ...")
                    stdscr.refresh()
                    curses.napms(1500)
                    break
def main(stdscr):
    system = StudentManageMentSystem()
    system.run(stdscr)
if __name__ == "__main__":
    curses.wrapper(main)