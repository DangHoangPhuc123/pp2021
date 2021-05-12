from zipfile import ZipFile
import os
import curses
from output import dp
from input import dp
from domain.student import * 
from domain.cousre import * 
from domain.mark import *
 
dhp= curses.initscr() 

def runcode():  
        dhp.addstr("Start Programming")
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
        dp.listStudents()
        dp.listCourses()
        dp.listMarks()
        dp.gpadecending()   
        while True:
            dhp.addstr("1. Zipfile")
            dhp.addstr("2. Load file again!")
            count=int(dhp.getstr().decode())
            if count ==1:
                list=['Students.txt','Courses.txt','Marks.txt']
                with ZipFile('students.dat','w') as zip:
                        for filename in list:
                            zip.write(filename)
                        for filename in list:
                            os.remove(filename)       
            elif count ==2:
                if os.path.isfile('student.dat'):
                    dhp.addstr("file exist\n")
                    zip_file = ZipFile('students.dat', 'r')
                    zip_file.extractall()
                    if os.path.isfile('students.txt'):     # load data from students.txt
                             stu= open('students.txt', 'r').readline()
                    if os.path.isfile('courses.txt'):     # load data from courses.txt
                             cou= open('courses.txt', 'r').readline()
                    if os.path.isfile('marks.txt'):      # load data from marks.txt
                             mar= open('marks.txt', 'r').readline()
                                                       
             
if __name__ == '__main__':
    runcode()
    