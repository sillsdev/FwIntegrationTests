cmd ="C:\Program Files (x86)\SIL\FieldWorks 8\Flex.exe" 
openApp(cmd)
wait(8)
click("1469790217759.png")
wait(3)
click(Pattern("1469790789522.png").similar(0.80))
find("1469793155809.png"),highlight(2)
click("1469793121673.png")
wheel(WHEEL_DOWN, 1)  # Scrolls down 1 times 
click("1469793269423.png")
click("1469793286342.png")
wait(2)
type("root based-sfm")
click("1469793900690.png")
click("1469793879730.png")
# next script for importing this file.