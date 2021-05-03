import math
import numpy as np
import curses

Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Credit=[]
Mark=[]
value=[]
Gpa=[]

dhp= curses.initscr() 

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
class dp:
    def numstudent():
        stu= dhp.addstr("Let's enter the numbers of student:\n")
        stu = int(dhp.getstr().decode())
        if stu> 0:
                return stu
        else:
                dhp.addstr("Should stop!!!")
                return 0
             
         
    def numcourses():
            cou = dhp.addstr("Let's enter the numbers of course:")
            cou = int(dhp.getstr().decode())
            if cou > 0:
                return cou
            else:
                dhp.addstr("Should stop!!!")
                return 0
         
    def inputstudent():
        dhp.addstr("Enter the information of student\n")
        dhp.refresh()
        dhp.addstr("enter ID student:\n")
        id=dhp.getstr().decode()
        dhp.refresh()
        dhp.addstr("Enter Name:\n")
        name=dhp.getstr().decode()
        dhp.refresh()
        dhp.addstr("Enter date of brith:\n")
        dob=dhp.getstr().decode()
        dhp.refresh()
        Student_s(id,name,dob)
    
    def inputCourses():
        dhp.addstr("Enter the information of courses\n")
        dhp.refresh()
        dhp.addstr("Enter ID course:\n")
        cID=dhp.getstr().decode()
        dhp.refresh()
        dhp.addstr("Enter CourseName:\n")
        name=dhp.getstr().decode()
        dhp.refresh()
        dhp.addstr("Enter CourseCredit:\n")
        credit=float(dhp.getstr().decode())
        dhp.refresh()
        Course_s(cID,name,credit)
         
    def Marks():
        dhp.addstr("enter courses id: ")
        cID = dhp.getstr().decode()
        dhp.refresh()
        if cID in CoursesID:
            dhp.addstr(" Enter student id:")
            id=dhp.getstr().decode()
            dhp.refresh()
            if id in StudentID:           
                dhp.addstr(" input mark: (0->20)")
                mark=math.floor(float(dhp.getstr().decode()))
            else:
                exit()
        else:
            exit() 
        mark_s(cID,id,mark)
         

    def Gpa():
        point=np.array([value])
        credits=np.array([Credit])
        dhp.addstr("enter student id:\n")
        id =dhp.getstr().decode()
        if id in StudentID:
            for i in range(0,len(Students)):
                totalCredit=np.sum(credits)
                totalValue=np.dot(point,credits)
                dhp.refresh()
            gpa=totalValue/totalCredit
        else: 
            return 0
        Gpa.append(gpa)
        for mark in Mark:
            dhp.refresh()
            dhp.addstr(" Mark_studentid:  [%s]   Gpa: [%s] \n" %(mark.get_id(),gpa))
            dhp.refresh()
            break
    
    def listCourses():
        dhp.addstr("lists of Courses:\n")
        dhp.refresh()
        for course in Courses:
            dhp.addstr("CourseID:  [%s]     CourseName:  [%s]     Credits:  [%s]\n" % (course.get_cID(), course.get_name(), course.get_credit()))
            dhp.refresh()
            
    def listStudent():
         dhp.addstr("lists of student:\n")
         dhp.refresh()
         for student in Students:
            dhp.addstr("Studentid:  [%s]    StudentName:  [%s]     dob:  [%s] \n" % (student.get_id(), student.get_name(), student.get_dob()))
            dhp.refresh()
               
    def listMarks():
        dhp.addstr("lists of mark:\n")
        dhp.refresh()
        for mark in Mark:
            dhp.addstr("coursesid:  [%s]    studentid: [%s]    mark:  [%s]\n" % (mark.get_cID(), mark.get_id(), mark.get_marks()))
            dhp.refresh()
            
    def gpadecending():
            array=np.array([Gpa])  
            array[::-1].sort()
            dhp.addstr("list sorting is %s: \n"%(array))
            dhp.refresh()

def runcode():  
    Nco=dp.numcourses()
    dhp.refresh()
    for i in range( Nco):
        dhp.addstr(f"Course { i+1}\n")
        dp.inputCourses()
        dhp.refresh()
        dhp.clear()
        Num=dp.numstudent()
        dhp.refresh()
        for i in range(Num):
            dhp.addstr(f"Student {i +1}:\n")
            dp.inputstudent()
            dhp.clear()
            dhp.refresh()
            dp.Marks() 
            dhp.clear()
            dhp.refresh()   
            break
    dp.Gpa()
    dp.listStudent()
    dp.listCourses()
    dp.listMarks()
    dp.gpadecending()
                                                 
             
if __name__ == '__main__':
  
    runcode()
    