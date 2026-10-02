from domains.Person import Person
class Student(Person):
    def __init__(self, student_id = "", name = "", dob = ""):
        super().__init__(student_id, name)
        self.__dob = dob
        self.gpa = 0.0
    def get_dob(self):
        return self.__dob