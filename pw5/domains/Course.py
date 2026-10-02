from domains.Person import Person
class Course(Person):
    def __init__(self, course_id = "", name = "", credits = 0): 
        super().__init__(course_id, name)
        self.credits = credits
    def get_credits(self):
        return self.credits