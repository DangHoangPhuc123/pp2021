Mark=[]
value=[]
Gpa=[]

class mark_s:
    def __init__(self,cID,id,marks,gpa=0):
        self.g=cID
        self.h=id
        self.i=marks
        self.k=gpa
        Mark.append(self)
        value.append(self.i)
        
    def get_cID(self):
        return self.g
    def get_id(self):
        return self.h
    def get_marks(self):     
        return self.i