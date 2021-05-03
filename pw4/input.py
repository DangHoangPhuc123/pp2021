import math
import numpy as np
import curses
from domain.student import * 
from domain.cousre import * 
from domain.mark import * 
dhp= curses.initscr() 
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