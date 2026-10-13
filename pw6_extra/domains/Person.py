class Person:
    def __init__(self, person_id = "", name = ""):
        self.person_id = person_id
        self.name = name
    def get_id(self):
        return self.person_id
    def get_name(self):
        return self.name