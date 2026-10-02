import curses
from domains import Person, Course, Student
from input import input_courses, input_marks, input_students
from output import list_courses, list_marks, list_students
import os
import zipfile

class StudentManageMentSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
        
    def load_data(self):
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zipf:
                zipf.extractall()
        if os.path.exists("students.txt"):
            with open ("students.txt", "r", encoding = "utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3: #check if there are 3 informations or not
                        self.__students.append(Student(parts[0], parts[1], parts[2])) #arrange
        if os.path.exists("courses.txt"):
            with open ("courses.txt", "r", encoding = "utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.__courses.append(Course(parts[0], parts[1], int(parts[2])))
        if os.path.exists("marks.txt"):
            with open ("marks.txt", "r", encoding = "utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        course_id, student_id, marks = parts[0], parts[1], float(parts[2])
                        if course_id not in self.__marks:
                            self.__marks[course_id] = {}
                            self.__marks[course_id][student_id] = marks

    def compress_data(self):
        txt_files = ["students.txt", "courses.txt", "marks.txt"]
        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
            for fname in txt_files:
                if os.path.exists(fname):
                    zipf.write(fname)
                    os.remove(fname)
    
    def run(self, stdscr):
            self.load_data()    
        
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
                stdscr.addstr("\n0. Exit")
                stdscr.addstr("\nEnter your choice (0-6)")
                stdscr.refresh() #update full info to user
                
                choice = stdscr.getkey() 
                if choice == '1':
                    input_students(stdscr, self.__students, Student)
                elif choice == '2':
                    input_courses(stdscr, self.__courses, Course)
                elif choice == '3':
                    input_marks(stdscr, self.__marks, self.__courses, self.__students)
                elif choice == '4':
                    list_students(stdscr, self.__students, self.__courses, self.__marks)
                elif choice == '5':
                    list_courses(stdscr, self.__courses)
                elif choice == '6':
                    list_marks(stdscr, self.__students, self.__marks, self.__courses)
                elif choice == '0':
                    self.compress_data()
                    break
def main(stdscr):
    system = StudentManageMentSystem()
    system.run(stdscr)
if __name__ == "__main__":
    curses.wrapper(main)