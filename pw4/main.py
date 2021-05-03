import curses
from output import dp
from input import dp
from domain.student import * 
from domain.cousre import * 
from domain.mark import *
 
dhp= curses.initscr() 

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
    