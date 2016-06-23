'''
from test_helper import *
import flex_helper
list = "Sena826ExampleWin 2016-04-27 1427 (1).fwbackup"
flex_helper.openFwBackup(list, 10)
'''
#Restore a project fucntionality is not working for the second time while running the above script
App.open("fieldworks")
click("1466425755754.png")
click("1466425919318.png")
click("1466425938739.png")
wait(5)
r = Region(158,23,765,555)
wait(2)
click("1466426737583.png")
wait(2)
click(Pattern("1466427073614.png").targetOffset(-59,-1))
wait(2)
click("1466426820079.png")
wait(2)
r1 = Region(178,193,743,775)
wait(2)
click(Pattern("1466427183020.png").targetOffset(-35,3))
wait(1)
click(Pattern("1466427210263.png").targetOffset(-38,0))
wait(1)
click("1466427258247.png")
r2= Region(189,636,796,318)
r2.find(Pattern("1466158277577.png").targetOffset(-16,6)).highlight(2)
if inside().find(Pattern("1466158277577.png").targetOffset(-16,6)).exists("1466157944386.png"):
    popup("Texts appears in Before Box - Expected")
else:
    popup(" Before texts are not found")
r2.find("1466427507610.png").highlight(2)
if inside().find(Pattern("1466427507610.png").targetOffset(-35,6)).exists("1466427550140.png"):  
     popup("Texts appears in After Box - Expected") 
else: 
     popup("After Texts are not found")
     
