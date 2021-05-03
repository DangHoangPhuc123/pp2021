
Students=[]
StudentID=[]

class Student_s:
    def __init__(self, s_id, name, dob):
        self.a=s_id
        self.b=name
        self.c=dob
        Students.append(self)
        StudentID.append(self.a)
    def get_id(self):
        return self.a
    def get_name(self):
        return self.b
    def get_dob(self):
        return self.c