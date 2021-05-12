Courses=[]
CoursesID=[]
Credit=[]

class Course_s:
    def __init__(self,cID,name,credit):
        self.d=cID
        self.e=name
        self.f=credit
        Courses.append(self)
        CoursesID.append(self.d)
        Credit.append(self.f)
        
    def get_cID(self):
        return self.d
    def get_name(self):
        return self.e
    def get_credit(self):
        return self.f