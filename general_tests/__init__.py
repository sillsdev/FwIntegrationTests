import unittest
import os
import imp

def load_tests(loader, standard_tests, pattern):
    for folder in os.listdir(os.path.dirname(__file__)):
        if "_sikuli_runall.sikuli" == folder:
            folder = os.path.join(os.path.dirname(__file__), folder)
            sikuliFolder = folder
            sikuliFile = os.path.basename(sikuliFolder)[:-7]+".py"
            wholePath = os.path.join(sikuliFolder,sikuliFile)
            name = os.path.basename(folder)[:-7]
            newfolder = os.path.dirname(folder)
            mod = imp.load_source("_sikuli_runall",wholePath)
            tests = loader.loadTestsFromName("MyTests",mod)
            standard_tests.addTests(tests)
    return standard_tests
