from test_helper import *
from sikuli import *

class CreateProject():
    

    def NewProject(self):
        wait(2)    
        App.open("fieldworks")
        wait(6)

        ### Creating FieldWorks Projects ###
        FindReg2 = find("CreateRegion.png")
        Below = FindReg2.below()
        rright = FindReg2.right()

        display1 = Region(Below.getX(), Below.getY(), Below.getW() + rright.getW(), Below.getH())
    #    display1.highlight(1)
        display1.find("CreateNW.png").click()

        newName = "DictionaryPane_Test"
        GetTimeNow = time.strftime ('%Y %m %d - %H%M%S')
        ProjectName = newName + GetTimeNow
        #print ProjectName     
    
        type(Pattern("ProjectName.png").targetOffset(-51,8), ProjectName)
        click("NewProjectOk.png")
        wait(4)
        FindReg3 = find("TextChoose.png")    
        B_below = FindReg3.below()
        L_Left = FindReg3.left()

        display2 = Region(L_Left.getX(), B_below.getY(), B_below.getW() + L_Left.getW(), B_below.getH())
    #   display2.highlight(1)
        
        display2.find("ChooseOk.png").click()
        wait("WaitLexiconPane.png", 60)

        