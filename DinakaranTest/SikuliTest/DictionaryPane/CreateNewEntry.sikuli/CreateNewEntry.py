from test_helper import *
from sikuli import *

class CreateNewEntry():

    def NewEntry(self, NameText):
        
        NE = 0
        while NE < 2:
            
            App.focus("fieldworks")
            type("e", Key.CTRL)
            assert exists("NewEntryBox.png")
        
            NewEntryHelp = find(Pattern("HelpButton.png").similar(0.90))
            Above = NewEntryHelp.above()
            lLeft = NewEntryHelp.left()
            InNewEntry = Region(lLeft.getX(), Above.getY(), Above.getW() + lLeft.getW(), Above.getH())
            #print InNewEntry
            #InNewEntry.highlight(1)

            wait(1)
            InNewEntry.find("LexemeForm4.png").click()
            #EnterText = NameText
            type(NameText)
            InNewEntry.find(Pattern("Mt1-1.png").targetOffset(20,10)).click()
            #InNewEntry.find("MorphemeType.png")
            InNewEntry.find(Pattern("InfixClick-1.png").targetOffset(-15,16)).click()
            wait(1)
            InNewEntry.find(Pattern("GlossText.png").targetOffset(-44,4)).click()
            type("Vaildate")
            InNewEntry.find(Pattern("Category2-1.png").targetOffset(28,10)).click()
            InNewEntry.find(Pattern("ProformVerb.png").targetOffset(-1,12)).click()
            find("Createbutton-1.png").click()
            wait(2)        
            NE = NE + 1





