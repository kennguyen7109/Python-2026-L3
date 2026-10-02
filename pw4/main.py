import curses
from domains import Person, Course, Student
from input import input_courses, input_marks, input_students
from output import list_courses, list_marks, list_students

class StudentManageMentSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
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
                    break
def main(stdscr):
    system = StudentManageMentSystem()
    system.run(stdscr)
if __name__ == "__main__":
    curses.wrapper(main)
