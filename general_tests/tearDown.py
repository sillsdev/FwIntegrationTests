## Copyright (c) 2016 SIL International
## This software is licensed under the MIT License (http://opensource.org/licenses/MIT)

"""
This file is used by _sikuli_runall.sikuli to close FLEx.
"""

from sikuli import *
from test_helper import *

if myOS == "L":
    App.close("mono")
elif myOS == "W":
    App.close("fieldworks")
