import os
import sys, re, traceback
from sikuli import *

class ErrorsTest():

    def FindFailed_Assertion_error(self): ## Find an image when It did not find in the screen. #
        FailedMessages = str(sys.exc_info())
        print FailedMessages
        ImageName_AssertionError = FailedMessages.split()[2]
        if "AssertionError()," == ImageName_AssertionError:
            #print ImageName_AssertionError
            ScriptPath = sys.argv[0]
            FullError = traceback.format_exc()
            GetFunctionName = FullError.split()[11]
            PrintStatement = 'The  ' + str(GetFunctionName) + ' function is failed because of ' + str(ImageName_AssertionError) + ' and this error appeared in ' + str(ScriptPath) + ' file. '
            print PrintStatement
        else:        
            ImageName_AssertionError = FailedMessages.split()[6]
            #print ImageName_AssertionError     
            ScriptPath = sys.argv[0]
            FullError = traceback.format_exc()
            GetFunctionName = FullError.split()[11]
            PrintStatement = 'The  ' + str(GetFunctionName) + ' function is failed. So, Please find a picture in  ' + str(ScriptPath) + ' path and ' + str(ImageName_AssertionError)  + ' image file is unable to find. ' 
            print PrintStatement
