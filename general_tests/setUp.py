## Copyright (c) 2016 SIL International
## This software is licensed under the MIT License (http://opensource.org/licenses/MIT)

"""
This file is used by _sikuli_runall.sikuli to remove all existing FLEx projects,
open FLEx, and create a new project.
"""

from sikuli import *
from test_helper import *
import subprocess

if myOS == "L":
    subprocess.call("sudo rm -Rf /home/vagrant/.local/share/fieldworks/Projects/*", shell=True)
    App.open("fieldworks-flex")
elif myOS == "W":
    subprocess.call("rd c:\ProgramData\SIL\FieldWorks\Projects\ /s /q", shell=True)
    subprocess.call("mkdir c:\ProgramData\SIL\FieldWorks\Projects\ ", shell=True)
    App.open("fieldworks")

runScript("./helpers/1_open_flex")
