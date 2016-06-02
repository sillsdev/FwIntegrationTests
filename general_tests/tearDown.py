from sikuli import *
from test_helper import *

if myOS == "L":
    App.close("mono")
elif myOS == "W":
    App.close("fieldworks")
