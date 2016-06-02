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
