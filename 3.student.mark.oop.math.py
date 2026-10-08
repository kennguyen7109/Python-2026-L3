import curses #library for designing terminal based applications
import math #library for mathematical functions
import numpy as np

class Person:
    def __init__(self, person_id = "", name = ""):
        self.person_id = person_id
        self.name = name
    def get_id(self):
        return self.person_id
    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, person_id = "", name = "", dob = ""):
        super().__init__(person_id, name)
        self.__dob = dob
        self.gpa = 0.0
    def get_dob(self):
        return self.__dob

class Course(Person):
    def __init__(self, course_id = "", name = "", credits = 0): 
        super().__init__(course_id, name)
        self.credits = credits
    def get_credits(self):
        return self.credits

class StudentManageMentSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
    def help_inputcurses(self, stdscr, prompt): #function to take input from user using curses library
        stdscr.addstr(prompt) #show prompt to user (stdscr = standard screen)
        stdscr.refresh() #update the screen to user
        curses.echo() #turn on echoing of characters typed by user
        user_input = stdscr.getstr().decode() #get input from user and decode it to string
        curses.noecho() #turn off echoing of characters typed by user to not inerrupt the screen
        return user_input #return the input from user
    def wait_keypress(self, stdscr): #function to wait for user to press any key
        stdscr.addstr("\nPress any key to continue...") #show message to user 
        stdscr.refresh() 
        stdscr.getch() #wait for user to press any key
    def input_students(self, stdscr):
        stdscr.clear() #clear the screen
        stdscr.addstr("---Input Student Information---")
        try:
            count = int(self.help_inputcurses(stdscr, "\nEnter number of students in a class: ")) #user enter number of students and convert to interger
        except ValueError:
            stdscr.addstr("\nInvalid input! Please enter a valid number!")
            self.wait_keypress(stdscr)
            return
        for i in range(count):
            stdscr.clear()
            stdscr.addstr(f"----Student Information #{i+1}----")
            student_id = self.help_inputcurses(stdscr, "\nStudent ID: ")
            student_name = self.help_inputcurses(stdscr, "Name: ")
            student_dob = self.help_inputcurses(stdscr, "Date of birth (DD/MM/YYYY): ")
            student = Student(student_id, student_name, student_dob) #create new student
            self.__students.append(student) #add new student to the students list
        stdscr.addstr("\nStudent Information input completed successfully!")
        self.wait_keypress(stdscr)
    def input_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("---Input Course Information---")
        try:
            count = int(self.help_inputcurses(stdscr, "\nEnter number of courses: "))
        except ValueError:
            stdscr.addstr("\nInvalid input! Please enter a valid number!")
            self.wait_keypress(stdscr)
            return
        for i in range(count):
            stdscr.clear()
            stdscr.addstr(f"----Course Information #{i+1}----")
            course_id = self.help_inputcurses(stdscr, "\nCourse ID: ")
            course_name = self.help_inputcurses(stdscr, "\nCourse Name: ")
            try:
                credits = int(self.help_inputcurses(stdscr, "\nCourse Credits: "))
            except ValueError:
                credits = 0
            course = Course(course_id, course_name, credits)
            self.__courses.append(course)
        stdscr.addstr("\nCourse Information input completed successfully!")
        self.wait_keypress(stdscr)
    def input_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr("---Input Marks---")
        if not self.__students or not self.__courses:
            stdscr.addstr("\nPlease input students and courses first!")
            self.wait_keypress(stdscr)
            return
        selected_course_id = self.help_inputcurses(stdscr, "\nEnter course ID to input marks: ")
        selected_course = any(selected_course_id == course.get_id() for course in self.__courses)
        if not selected_course:
            stdscr.addstr("\nCourse not found!")
            self.wait_keypress(stdscr)
            return
        if selected_course_id not in self.__marks:
            self.__marks[selected_course_id] = {}
        for students in self.__students:
            while True:
                try:
                    mark = float(self.help_inputcurses(stdscr, f"\nEnter mark for {students.get_name()} (ID: {students.get_id()}):"))
                    rounded_mark = math.floor(mark * 10) / 10.0 #rounded to 1 decimal number after ,
                    self.__marks[selected_course_id][students.get_id()] = rounded_mark #save point 
                    break
                except ValueError:
                    stdscr.addstr("\nInvalid mark! Please enter a valid number!")
        stdscr.addstr("\nMarks input completed successfully!")
        self.wait_keypress(stdscr)
    def calculated_gpa(self, student_id):
        mark_lists = []
        credits_list = []
        for course in self.__courses:
            course_id = course.get_id()
            if course_id in self.__marks and student_id in self.__marks[course_id]:
                mark_lists.append(self.__marks[course_id][student_id])
                credits_list.append(course.get_credits())
        if not credits_list or not sum(credits_list) == 0:
            return 0.0 #return 0.0 if there are no credits or the sum of credits is zero to avoid division by zero
        marks_np = np.array(mark_lists)
        credits_np = np.array(credits_list)
        gpa = np.sum(marks_np * credits_np) / np.sum(credits_np)
        return float(gpa)
    def sort_students_by_gpa(self):
        for student in self.__students:
            student.gpa = self.calculated_gpa(student.get_id())
        if not self.__students:
            return []
        gpa = np.array([student.gpa for student in self.__students])
        sorted_indices = np.argsort(gpa)[::-1] #sort in descending order
        sorted_students = [self.__students[i] for i in sorted_indices] #return sorted list of students based on GPA
        return sorted_students 
    def list_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("---List of Students (Sorted by GPA)---")
        if not self.__students:
            stdscr.addstr("\nNo students found!")
            self.wait_keypress(stdscr)
            return
        sorted_students = self.sort_students_by_gpa()
        for student in sorted_students:
            stdscr.addstr(f"\nID: {student.get_id()}, Name: {student.get_name()}, Date of Birth: {student.get_dob()}, GPA: {student.gpa:.2f}")
        self.wait_keypress(stdscr)
    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("---List of Courses---")
        if not self.__courses:
            stdscr.addstr("\nNo courses found!")
            self.wait_keypress(stdscr)
            return
        for course in self.__courses:
            stdscr.addstr(f"\nID: {course.get_id()}, Name: {course.get_name()}, Credits: {course.get_credits()}")
        self.wait_keypress(stdscr)
    def list_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr("---List of Marks---")
        if not self.__marks:
            stdscr.addstr("\nNo marks found!")
            self.wait_keypress(stdscr)
            return
        selected_course_id = self.help_inputcurses(stdscr, "\nEnter course ID: ")
        if selected_course_id not in self.__marks:
            stdscr.addstr("\nNo marks found!")
            self.wait_keypress(stdscr)
            return
        stdscr.addstr(f"\n----Marks for Courses {selected_course_id}----")
        course_marks = self.__marks[selected_course_id]
        for student in self.__students:
            student_id = student.get_id()
            mark = course_marks.get(student_id)
            stdscr.addstr(f"\nStudent ID: {student_id}, Name: {student.get_name()} ,Mark: {mark}")
        self.wait_keypress(stdscr)
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
                self.input_students(stdscr)
            elif choice == '2':
                self.input_courses(stdscr)
            elif choice == '3':
                self.input_marks(stdscr)
            elif choice == '4':
                self.list_students(stdscr)
            elif choice == '5':
                self.list_courses(stdscr)
            elif choice == '6':
                self.list_marks(stdscr)
            elif choice == '0':
                break
def main(stdscr):
    system = StudentManageMentSystem()
    system.run(stdscr)
if __name__ == "__main__":
    curses.wrapper(main)