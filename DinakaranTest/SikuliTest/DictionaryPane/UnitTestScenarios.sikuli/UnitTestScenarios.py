
import unittest
import HTMLTestRunner
import os
import sys, re, traceback
import inspect
from test_helper import *
from sikuli import *

myScriptDirectory = os.path.abspath(os.path.split(sys.argv[0])[0])
addImportPath(myScriptDirectory)
import CreateProject
import CreateNewEntry
import ShortCutKeys
import Errors
import MediaFile


class DictionsryPaneKeysTest(unittest.TestCase):

    def test_1_startup(self):
        try:
            CP = CreateProject.CreateProject()
            CP.NewProject()
            NE = CreateNewEntry.CreateNewEntry()
            NewEntry = "Builders"
            NE.NewEntry(NewEntry)           
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            assert False

    def test_2_Navigate(self):
        try:
            Navigate = ShortCutKeys.ShortCutKeysTest()
            Navigate.NavigateDictionaryPane()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            assert False
    
    def test_7_Findbox1(self):
        try:
            checkbox1 = ShortCutKeys.ShortCutKeysTest()
            checkbox1.Findbox1()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            #AFE.FindFailed_Assertion_error()
            assert False
                        
    def test_4_Findbox2(self):
        
        try:
            checkbox2 = ShortCutKeys.ShortCutKeysTest()        
            checkbox2.Findbox2()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            assert False

    def test_5_Delete(self):
        
        try: 
            Deletes = ShortCutKeys.ShortCutKeysTest()
            Deletes.Delete()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()    
            assert False

    def test_6_UndoRedo(self):
        
        try:
            UD = ShortCutKeys.ShortCutKeysTest()        
            UD.UndoRedo()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            assert False

    def test_3_NewEntryBox(self):

        try:      
            NE = ShortCutKeys.ShortCutKeysTest()        
            NE.NewEntryBox()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            assert False

    def test_8_ForwardBackward(self):

        try:   
            LR = ShortCutKeys.ShortCutKeysTest()
            LR.LeftandRight()
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error()
            assert False
  

class MediafileTest(unittest.TestCase):

    def test_1_Links(self):
        
        try:
            LK = MediaFile.LinkTest()
            LK.Links()                   
        except(FindFailed, AssertionError):
            ERR = Errors.ErrorsTest() 
            ERR.FindFailed_Assertion_error() 
            assert False    
  
    def test_2_Endup(self):
        App.close("fieldworks")


test_classes_to_run = [DictionsryPaneKeysTest, MediafileTest]
loader = unittest.TestLoader()
    
suites_list = []
for test_class in test_classes_to_run:    
    suite = loader.loadTestsFromTestCase(test_class)
    suites_list.append(suite)
    
big_suite = unittest.TestSuite(suites_list)

myScriptPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
CreateFile = os.path.expanduser(myScriptPath + "/SuiteReports.html")
outfile = open(CreateFile, "w")

runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title="Test Report", description="Directory Pane Scenarios Testing")
runner.run(big_suite)
outfile.close()


