import unittest2
import HTMLTestRunner
import os
import sys, re, traceback

class TestSeqFunc(unittest2.TestCase):  

  def test1(self):
    click("Field.png")
    assert True

  def test2(self):
    click("Field.png")
    assert False

suite = unittest2.TestLoader().loadTestsFromTestCase(TestSeqFunc)
#CreateFile = os.path.expanduser("~/Desktop/Report.html")
#outfile = open(CreateFile, "w")
#runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title="Test Report", description="Test1")
runner.run(suite)

