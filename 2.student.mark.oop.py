class Person: #base class stand for representing a person
    def __init__(self, person_id="", name=""):
        self.person_id = person_id
        self.name = name
#Encapsulation (using getter methods)    
    def get_id(self):
        return self.person_id
    def get_name(self):
        return self.name
#Polymorphism (using method overriding)
    def input(self):
        pass
    def list(self):
        pass

class Student(Person): #subclass stand for representing a student which inherits from Personclass
    def __init__(self, student_id="", name = "", dob = ""):
        super().__init__(student_id, name) #call the constructor of bass class to initialize the inherited attributes
        self.__dob = dob #__ make dob private attribute, can only be accessed in the class Student
    def get_dob(self):
        return self.__dob #getter method to take dob
    def input(self):
        self.person_id = input("Student ID: ")
        self.name = input("Name: ")
        self.__dob = input("Date of birth (DD/MM/YYYY): ").strip()
    def list(self):
        print(f"Student ID: {self.person_id}, Name: {self.name}, Date of birth: {self.__dob}")

class Course(Person): 
    def __init__(self, course_id = "", name = ""):
        super().__init__(course_id, name)
    def input(self):
        self.course_id = input("Course ID: ").strip()
        self.name = input("Course Name: ").strip()
    def list(self):
        print(f"Course ID: {self.course_id}, Name: {self.name}")
        
class Mark:
    def __init__(self, course_id = "", student_id = "", mark = 0.0):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark
    def input(self):
        self.course_id = input("Course ID : ").strip()
        self.student_id = input("Student ID : ").strip()
        self.mark = float(input("Mark : ").strip())
    def list(self):
        print(f"Course ID: {self.course_id}, Student ID: {self.student_id}, Mark: {self.mark}")

class StudentManagementSystem:
    def __init__(self):
        self.__students = [] #declare private attributes to hide the date from outside of the class 
        self.__courses = []
        self.__marks = {} 
    def input_students(self):
        try: #make sure the input is valid number, if not, print error message and return
            number_students = int(input("Enter number of students in a class: "))
        except ValueError:
            print("Invalid input! Please enter a valid number!")
            return
        for i in range(number_students):
            print(f"\n----Student Information #{i+1}----")
            student = Student()
            student.input()
            self.__students.append(student) #make new student object and add it to the students list
    def input_courses(self):
        try:
            number_courses = int(input("Enter number of courses: "))
        except ValueError:
            print("Invalid input! Please enter a valid number!")
            return
        for i in range(number_courses):
            print(f"\n----Course Information #{i+1}----")
            course = Course()
            course.input()
            self.__courses.append(course) #make new course object and add it to the courses list
    def input_marks(self):
        if not self.__students:
            print("\nNo student information! Please enter student information first!")
            return
        if not self.__courses:
            print("\nNo course found! Please enter courses first!")
            return
        self.list_courses()
        selected_course_id = input("\nEnter ID of the course to input marks: ").strip()
        course_exists = any(c.get_id() == selected_course_id for c in self.__courses)
        if not course_exists:
            print("Course not found!")
            return
        if selected_course_id not in self.__marks:
            self.__marks[selected_course_id] = {}
        print(f"\n----Input marks for course {selected_course_id}----")
        for student in self.__students:
            try:
                mark = float(input(f"Marks for student {student.get_name()} (ID: {student.get_id()}): "))
                self.__marks[selected_course_id][student.get_id()] = mark
            except ValueError:
                print("Invalid input! Please enter a valid number!")
    def list_students(self):
        print("\n----List of Students----")
        if not self.__students:
            print("No student information available.")
            return
        for student in self.__students:
            student.list()
    def list_courses(self):
        print("\n----List of Courses----")
        if not self.__courses:
            print("No course information available.")
            return
        for course in self.__courses:
            course.list()
    def show_student_marks(self):
        if not self.__marks:
            print("\nNo marks available! Please enter marks first!")
            return
        selected_course_id = input("\nEnter ID of the course to show marks: ").strip()
        if selected_course_id not in self.__marks:
            print("No marks found for this course!")
            return
        print(f"\n----Marks for course {selected_course_id}----")
        for student in self.__students:
            student_id = student.get.id()
            mark = self.__marks[selected_course_id].get(student_id, "N/A")
            print(f"Student ID: {student_id}, Name: {student.get_name()}, Mark: {mark}")
    
    def run(self):
        while True:
            print("\n----Student Management System Menu----")
            print("1. Input Student Information")
            print("2. Input Course Information")
            print("3. Input Marks")
            print("4. List Students")
            print("5. List Courses")
            print("6. Show Student Marks for a course")
            print("0. Exit")
            choice = input("Enter your choice (0-6): ").strip()
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice =='3':
                self.input_marks()
            elif choice == '4':
                self.list_students()
            elif choice == '5':
                self.list_courses()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '0':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice! Please enter a number between 0 and 6.")

if __name__ == "__main__": # run the program if this file is executed directly
    app = StudentManagementSystem() # create an instance of the StudentManagementSystem class
    app.run() # call the run method to start the program