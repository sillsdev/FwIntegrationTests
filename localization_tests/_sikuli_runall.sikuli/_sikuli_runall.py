## Copyright (c) 2016 SIL International
## This software is licensed under the MIT License (http://opensource.org/licenses/MIT)

"""
_sikuli_runall is used to dynamically create a test class of tests from sikuli files collocated with it.
It is used in conjunction with __init__.py file to find tests, setUp.py for setup and tearDown for teardown of tests.
"""

import xmlrunner
import sys
import unittest
import subprocess
import os
import inspect
import runpy
import sikuli
import test_helper

class MyTests(unittest.TestCase):

    if __name__ == '__main__':
        myFolder = sikuli.getParentFolder()
    else:
        if test_helper.myOS == "L":
            myFolder = os.path.dirname(__file__)
        elif test_helper.myOS == "W":
            myFolder = os.path.dirname(os.path.dirname(__file__))
        elif test_helper.myOS == "M":
            myFolder = os.path.dirname(__file__)

    def setUp(self):
        print "setup"
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
        return_code = test_helper.runScript(file)
        if return_code != 0:
            raise Exception('The Sikuli script did not exit cleanly.')
        return test_helper.getLastLogLine()

def make_method(name, skipFlag):
    @unittest.skipIf(skipFlag, name+" is not being run")
    def my_method(self):
        #print("method {0} in {1}".format(name, self))
        output = self.run_sikuli_test(self.id())
        self.assertFalse(' --- ' in output)
    return my_method

for folder in os.listdir(MyTests.myFolder):
    if folder.startswith("#"):
        name = folder[1:-7]
        skipFlag = True
    else:
        name = folder[:-7]
        skipFlag = False
    if  folder.endswith(".sikuli") and not folder.startswith("_"):
        _method = make_method(name, skipFlag)
        setattr(MyTests, "test_"+name, _method)

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(".", pattern="__init__.py")
    if test_helper.myOS == "L":
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTests))
    if len(sys.argv)<2 or sys.argv[1] == "text":
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif sys.argv[1] == "xml":
        with file(os.path.join(sikuli.getParentFolder()+"unittest.xml"), "w") as f:
            xmlrunner.XMLTestRunner(f).run(suite)
    elif sys.argv[1] == "moveImages":
        test_helper.moveImagesToCommonFolder()
    else:
        print "invalid run mode for _runall"
