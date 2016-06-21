import os
import sys, re, traceback
import shutil
from test_helper import *

## Summary: Crash on category edit pane when click "Ok" button on "Choose inflectional feature" dialog box. ##
## Creating New FieldWorks Project ##
def NewProject():
    wait(2)    
    App.open("fieldworks")
    wait(6)

    ### Creating region on "Language Explorer" dialog box ###
    FindReg2 = find("CreateRegion.png")
    Below = FindReg2.below()
    rright = FindReg2.right()
    display1 = Region(Below.getX(), Below.getY(), Below.getW() + rright.getW(), Below.getH())
    display1.highlight(1)
    display1.find(Pattern("CreateNW.png").similar(0.90)).click()

    newName = "Choose inflectional feature_16220_"
    GetTimeNow = time.strftime ('%Y %m %d - %H%M%S')
    ProjectName = newName + GetTimeNow
    print ProjectName     
    
    ## Creating Region for "New FieldWorks Project" dialog box #
    FindReg4 = find("NewDialogRegion.png")
    Below = FindReg4.below()
    rright = FindReg4.right()
    display3 = Region(Below.getX(), Below.getY(), Below.getW() + rright.getW(), Below.getH())
    display3.highlight(1)
    
    display3.find(Pattern("NewPro.png").similar(0.90)).type(ProjectName)
    display3.find(Pattern("ClickOkNew.png").similar(0.90)).click()
    wait(4)
    
    ## Creating Region for "Choose a List of Anthropology Categories" dialog box. #    
    FindReg3 = find("TextChoose.png")    
    B_below = FindReg3.below()
    L_Left = FindReg3.left()
    display2 = Region(L_Left.getX(), B_below.getY(), B_below.getW() + L_Left.getW(), B_below.getH())
    display2.highlight(1)
    
    display2.find(Pattern("ChooseListOk.png").similar(0.90)).click()
    wait(2)

## Creating New Stem_Name for category ###
def Category_Stem_Name():
    wait("LexiconPane.png", 30)
    click("GrammarPane.png")
    wait("Grammarlists.png", 10)
    find("CategoryEdit.png").click()
    find(Pattern("NounTest.png").similar(0.90)).click()
    ## Creating Region for right side "Category" pane.
    Category = find("CategoryRight.png")
    Below = Category.below()
    rright = Category.right()
    NounStem = Region(Below.getX(), Below.getY(), Below.getW() + rright.getW(), Below.getH())
#    NounStem.highlight(1)
    
    NounStem.find("StemNames.png").click()
    NounStem.find("InsertStem.png").click()
    NounStem.wait(Pattern("FeatureSet.png").similar(0.90),6)
    NounStem.find(Pattern("FeatureSet.png").similar(0.90)).click()
    NounStem.find("ThreedotsFeatures.png").click()
    wait("InflectionFeaturesforNoun.png", 10)
    find("OkClick.png").click()
    NounStem.find("StemNameField.png").click()


def GetGreen_Text(): # Creating text file on desktop for error stack lines when green crash appears. #
    CreateFile = os.path.expanduser("~/Desktop/LT-16220.txt")
    Open_file = open(CreateFile, "wb+")
    getclip = Env.getClipboard()
#    print getclip
    Open_file.write(getclip)
    out = Open_file.read()
    Open_file.close()

def Green_Stack_Image(): # Creating screenshot on desktop when green crash appears #

    find("ViewDetails.png").click()
    screen = Screen()
    file = screen.capture(screen.getScreen())    
    print("Saved screen as "+file)
    shutil.move(file, os.path.expanduser(r"~\Desktop\LT-16220.png"))

    if exists(Pattern("CopyInfo.png").similar(0.90)):
        
        click(Pattern("Radioselect.png").similar(0.90))
        click(Pattern("ExitAPP1.png").similar(0.90))
        wait(2)
        GetGreen_Text()
    else:
        print "There is no green crash appear"

def findfailederror(): ## Find an image when It did not find in the screen. #
    err = str(sys.exc_info()[1])
    errs = err.split()[4]
    pth = sys.argv[0]
    ful_err = traceback.format_exc()
    vrie = ful_err.split()[11]
    PTR = 'This ' + str(vrie) + ' field is failed. So, Please find a picture in ' + str(pth) + str(errs) + ' path. ' 
    print PTR 

## Exception handling for all method when an image is failed to find. #
try:
    NewProject()
    Category_Stem_Name()

except FindFailed:
    
    Green_Stack_Image()    
    findfailederror()
    