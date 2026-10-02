import numpy as np
from input import help_inputcurses, wait_keypress
def calculated_gpa(students, courses, marks):
        mark_lists = []
        credits_list = []
        for course in courses:
            course_id = course.get_id()
            for student in students:
                student_id = student.get_id()
                if course_id in marks and student_id in marks[course_id]:
                    mark_lists.append(marks[course_id][student_id])
                    credits_list.append(course.get_credits())
        if not credits_list or not sum(credits_list) == 0:
            return 0.0 #return 0.0 if there are no credits or the sum of credits is zero to avoid division by zero
        marks_np = np.array(mark_lists)
        credits_np = np.array(credits_list)
        gpa = np.sum(marks_np * credits_np) / np.sum(credits_np)
        return float(gpa)
def sort_students_by_gpa(students, courses, marks):
        for student in students:
            student.gpa = calculated_gpa(student.get_id(), courses, marks)
        if not students:
            return []
        gpa = np.array([student.gpa for student in students])
        sorted_indices = np.argsort(gpa)[::-1] #sort in descending order
        sorted_students = [students[i] for i in sorted_indices] #return sorted list of students based on GPA
        return sorted_students 
def list_students(stdscr, students, courses, marks):
    stdscr.clear()
    stdscr.addstr("=== LIST OF STUDENTS (SORTED BY GPA) ===\n\n")
    if not students:
        stdscr.addstr("No students found!\n")
    else:
        sorted_list = sort_students_by_gpa(students, courses, marks)
        for student in sorted_list:
            stdscr.addstr(f"ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_dob()} | GPA: {student.gpa:.2f}\n")
    wait_keypress(stdscr)
def list_courses(stdscr, courses):
        stdscr.clear()
        stdscr.addstr("---List of Courses---")
        if not courses:
            stdscr.addstr("\nNo courses found!")
            wait_keypress(stdscr)
            return
        for course in courses:
            stdscr.addstr(f"\nID: {course.get_id()}, Name: {course.get_name()}, Credits: {course.get_credits()}")
            wait_keypress(stdscr)
def list_marks(stdscr, students, courses, marks):
    stdscr.clear()
    stdscr.addstr("=== SHOW MARKS ===\n\n")
    if not marks:
        stdscr.addstr("No marks found!\n")
        wait_keypress(stdscr)
        return
    selected_course_id = help_inputcurses(stdscr, "Enter course ID: ")
    if selected_course_id not in marks:
        stdscr.addstr("\nNo marks found for this course!")
        wait_keypress(stdscr)
        return
    stdscr.addstr(f"\n---- Marks for Course {selected_course_id} ----\n")
    for student in students:
        s_id = student.get_id()
        mark = marks[selected_course_id].get(s_id, "N/A")
        stdscr.addstr(f"Student ID: {s_id} | Name: {student.get_name()} | Mark: {mark}\n")
    wait_keypress(stdscr)