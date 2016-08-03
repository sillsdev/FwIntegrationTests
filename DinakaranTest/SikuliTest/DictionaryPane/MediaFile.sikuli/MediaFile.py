from test_helper import *
from sikuli import *

class LinkTest():

    def Links(self):      
        find("ViewClick.png").click()  
        find("ViewLexicon.png").click()
        find("ViewLexiconEdit.png").click()
        
        find("ClickTextsWords.png").click()
        find(Pattern("EditMenu.png").similar(0.80)).click()
        find("CopyLink.png").click()
        find("ClickLexicon.png").click()
        
        find("ClickNote.png").click()
        type("Links")
        type("a", Key.CTRL)
        find(Pattern("EditMenu.png").similar(0.80)).click()
        find(Pattern("PasteClick.png").targetOffset(-61,-10)).click()

        find("DictionaryClick.png").click()
        wait("WaitDictionary.png")
        
        find("ClickTools.png").click()
        find("ClickConfigure.png").click()
        find("ClickDictionaryOpen.png").click()      
        wait("WaitClickView.png")
        find(Pattern("CheckNote.png").similar(0.90).targetOffset(-12,1)).click()
        find("ClickOk.png").click()
        wait("CheckLinkTest.png", 5)
        assert exists("CheckLinkTest.png")
        
        find("CheckLinkTest.png").click()
        wait(2)
        assert exists("FindTextsWords.png")
        
        
