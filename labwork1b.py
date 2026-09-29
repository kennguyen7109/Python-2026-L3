students = []
course = []
marks = []

## INPUT FUNCTIONS
def input_number_of_students():
    return int(input("Enter number of students in a class: "))
def input_student_info():
    number_students = input_number_of_students()
    for i in range (number_students):
        print(f"----Student Information #{i+1}----")
        student_id = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of birth: ")
        students.append({
            "id": student_id,
            "name": name,
            "dob": dob 
        })

def input_number_of_course():
    return int(input("Enter number of courses: "))
def input_course_info():
    number_courses = input_number_of_students()
    for i in range (number_courses):
        print(f"\n----Courses Information #{i+1}----")
        course_id = input("Course ID: ").strip()
        course_name = input("Course: ").strip()
        course.append({
            "id": course_id,
            "name": course_name,
        })
        
def input_marks():
    if not students:
        print("\nNo student Information! Please enter student information first!")
        return
    if not course:
        print("\nNo course found! Please enter courses first!")
        return
    
    list_courses()
    selected_course_id = input("\nEnter ID courses that need mark: ").strip()
    
    course_exists = any(c['id'] == selected_course_id for c in course)
    if not course_exists:
        print("Course not found!")
        return
    if selected_course_id not in marks:
        marks[selected_course_id] = {}
        
    print(f"\n----Input marks for course {selected_course_id}----")
    for student in students:
        mark = float(input(f"Marks for student {student['name']} (ID: {student['id']}): "))
        marks[selected_course_id][student['id']] = mark
        
## LISTING FUNCTIONS
def list_courses():
    print("\n----List of course----")
    if not course:
        print("No course information found!")
        return
    for c in course:
        print(f"ID: {c['id']: < 10}\nCourse name: {c['name']}")

def list_students():
    print("\n----List of students----")
    if not students:
        print("No students information found!")
        return
    for s in students:
        print(f"ID: {s['id']: < 10}\nName: {s['name']}\nDate of birth: {s['dob']}")

def show_student_marks():
    if not marks:
        print("\nNo marks has been input!")
        return
    selected_course_id = input("\nEnter Course ID that need check marks: ").strip()
    if selected_course_id not in marks:
        print("\nNo marks information for this course!")
        return
    print(f"\n----Grade sheet {selected_course_id}----")
    for student in students:
        student_id = student['id']
        mark = marks[selected_course_id].get(student_id, "N/A")
        print(f"ID: {student_id}\nName: {student['name']}\nMark: {mark}")
    
## MAINN
def main():
    while True:
        print("STUDENT MARK MANAGEMENT")
        print("1. Enter student list")
        print("2. Enter course list")
        print("3. Enter mark for a course")
        print("4. Show student list")
        print("5. Show course list")
        print("6. Show mark list by course")
        print("0. Out")
        
        choice = input("Enter your choice(0-6): ").strip()
        
        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_course_info()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Out student management system")
            break
        else:
            print("Choice invalid, please choose again!")
if __name__ == "__main__":
    main()