from test_helper import *
App.open("fieldworks")
click("1466073587237.png")
click("1466073628193.png")
click("1466073661806.png")
wait(5)
click("1466073776284.png")
click("1466073851543.png")
rightClick("1467025161534.png")
click("1466073950840.png")
click("1466073999067.png")
click(Pattern("1467025250303.png").similar(0.80).targetOffset(-4,0))
click("1466074308443.png")
r1= Region(321,190,630,619)
r1.click(Pattern("1467025437284.png").similar(0.80))
wait(5)
click("1466074635013.png")
wait(5)
r2 = Region(301,181,691,655)
if r2.find("1467026980808.png").highlight(2):
    popup("Green Crash Appears!")
else:
    popup("This issue has been fixed")

