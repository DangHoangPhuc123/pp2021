import math
import numpy as np
import curses
from domain.student import * 
from domain.cousre import * 
from domain.mark import * 
dhp= curses.initscr() 
class dp:
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