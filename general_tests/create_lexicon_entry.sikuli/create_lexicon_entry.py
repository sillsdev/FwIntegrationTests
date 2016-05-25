from test_helper import *

# Opening
#############
wait("Lexicon.png",3)
click("Lexicon.png")
LEFT_SIDEBAR.wait("LexiconEdit.png", 3)
LEFT_SIDEBAR.click("LexiconEdit.png")
MID_TOOLBAR.click("Headword.png")
TOOLBARS.click("1435675185765.png")

# Goal
#############
type("cat")
wait(10)
type(Key.ENTER)
Region(147,101,537,692).exists("catcat.png")

