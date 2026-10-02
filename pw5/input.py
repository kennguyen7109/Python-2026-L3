import curses
import math

def save_students_txt(students):
    with open("students.txt", "w", encoding = "utf-8") as f:
        for student in students:
            f.write(f"{student.get_id()}, {student.get_name()}, {student.get_dob}")
def save_courses_txt(courses):
    with open("courses.txt", "w", encoding = "utf-8") as f:
        for course in courses:
            f.write(f"{course.get_id()}, {course.get_name()}")
def save_marks_txt(marks):
    with open("marks.txt", "w", encoding = "utf-8") as f:
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                f.write(f"{course_id}, {student_id}, {mark}")

def help_inputcurses(stdscr, prompt): #function to take input from user using curses library
        stdscr.addstr(prompt) #show prompt to user (stdscr = standard screen)
        stdscr.refresh() #update the screen to user
        curses.echo() #turn on echoing of characters typed by user
        user_input = stdscr.getstr().decode() #get input from user and decode it to string
        curses.noecho() #turn off echoing of characters typed by user to not inerrupt the screen
        return user_input #return the input from user
def wait_keypress(stdscr): #function to wait for user to press any key
        stdscr.addstr("\nPress any key to continue...") #show message to user 
        stdscr.refresh() 
        stdscr.getch() #wait for user to press any key

def input_students(stdscr, students, Student):
        stdscr.clear() #clear the screen
        stdscr.addstr("---Input Student Information---")
        try:
            count = int(help_inputcurses(stdscr, "\nEnter number of students in a class: ")) #user enter number of students and convert to interger
        except ValueError:
            stdscr.addstr("\nInvalid input! Please enter a valid number!")
            wait_keypress(stdscr)
            return
        for i in range(count):
            stdscr.clear()
            stdscr.addstr(f"----Student Information #{i+1}----")
            student_id = help_inputcurses(stdscr, "\nStudent ID: ")
            student_name = help_inputcurses(stdscr, "Name: ")
            student_dob = help_inputcurses(stdscr, "Date of birth (DD/MM/YYYY): ")
            student = Student(student_id, student_name, student_dob) #create new student
            students.append(student) #add new student to the students list
        save_students_txt(students)
        stdscr.addstr("\nStudent Information input and saved to txt file completed successfully!")
        wait_keypress(stdscr)

def input_courses(stdscr, courses, Course):
        stdscr.clear()
        stdscr.addstr("---Input Course Information---")
        try:
            count = int(help_inputcurses(stdscr, "\nEnter number of courses: "))
        except ValueError:
            stdscr.addstr("\nInvalid input! Please enter a valid number!")
            wait_keypress(stdscr)
            return
        for i in range(count):
            stdscr.clear()
            stdscr.addstr(f"----Course Information #{i+1}----")
            course_id = help_inputcurses(stdscr, "\nCourse ID: ")
            course_name = help_inputcurses(stdscr, "\nCourse Name: ")
            try:
                credits = int(help_inputcurses(stdscr, "\nCourse Credits: "))
            except ValueError:
                credits = 0
            course = Course(course_id, course_name, credits)
            courses.append(course)
        save_courses_txt(courses)
        stdscr.addstr("\nCourse Information input and saved to txt file completed successfully!")
        wait_keypress(stdscr)

def input_marks(stdscr, students, courses, marks):
        stdscr.clear()
        stdscr.addstr("---Input Marks---")
        if not students or not courses:
            stdscr.addstr("\nPlease input students and courses first!")
            wait_keypress(stdscr)
            return
        selected_course_id = help_inputcurses(stdscr, "\nEnter course ID to input marks: ")
        selected_course = any(selected_course_id == course.get_id() for course in courses)
        if not selected_course:
            stdscr.addstr("\nCourse not found!")
            wait_keypress(stdscr)
            return
        if selected_course_id not in marks:
            marks[selected_course_id] = {}
        for student in students:
            while True:
                try:
                    mark = float(help_inputcurses(stdscr, f"\nEnter mark for {student.get_name()} (ID: {student.get_id()}):"))
                    rounded_mark = math.floor(mark * 10) / 10.0 #rounded to 1 decimal number after ,
                    marks[selected_course_id][student.get_id()] = rounded_mark #save point 
                    break
                except ValueError:
                    stdscr.addstr("\nInvalid mark! Please enter a valid number!")
        save_marks_txt(marks)
        stdscr.addstr("\nMarks input and saved to txt file completed successfully!")
        wait_keypress(stdscr)