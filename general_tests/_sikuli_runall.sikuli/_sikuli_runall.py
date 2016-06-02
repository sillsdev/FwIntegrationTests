import xmlrunner
import sys
import unittest
import subprocess
import os
import inspect
import runpy
from sikuli import *
from test_helper import *

class MyTests(unittest.TestCase):

    if __name__ == '__main__':
        myFolder = getParentFolder()
    else:
        if myOS == "L":
            myFolder = os.path.dirname(__file__)
        elif myOS == "W":
            myFolder = os.path.dirname(os.path.dirname(__file__))
        elif myOS == "M":
            myFolder = os.path.dirname(__file__)

    def setUp(self):
        try:
            runpy.run_path(os.path.join(MyTests.myFolder,"setUp.py"))
        except IOError:
            pass

    def tearDown(self):
        try:
            runpy.run_path(os.path.join(MyTests.myFolder,"tearDown.py"))
        except IOError:
            pass

    def run_sikuli_test(self,name):
        the_test = str.split(name,".")[-1][5:] # test name of the form '__main__.MyTests.test_name', split on periods, then remove the 'test_'
        file = os.path.join(MyTests.myFolder, the_test+".sikuli") # test location
        return_code = runScript(file)
        if return_code != 0:
            raise Exception('The Sikuli script did not exit cleanly.')
        last = ""
        if os.path.exists(error_file):
            for line in open(error_file):
                last = line
            return last
        else:
            return ""

def make_method(name):
    def my_method(self):
        #print("method {0} in {1}".format(name, self))
        output = self.run_sikuli_test(self.id())
        self.assertFalse(' --- ' in output)
    return my_method

for folder in os.listdir(MyTests.myFolder):
    name = folder[:-7]
    if ".sikuli" == folder[-7:] and not "_" == folder[0] and not "#" == folder[0] :
        _method = make_method(name)
        setattr(MyTests, "test_"+name, _method)

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(".", pattern="*.py")
    if myOS == "L":
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTests))
    if len(sys.argv)<2 or sys.argv[1] == "text":
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif sys.argv[1] == "xml":
        with file(os.path.join(getParentFolder()+"unittest.xml"), "w") as f:
            xmlrunner.XMLTestRunner(f).run(suite)
    else:
        print "invalid run mode for _runall"
