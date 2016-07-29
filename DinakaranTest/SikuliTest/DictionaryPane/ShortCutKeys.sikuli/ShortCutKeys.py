from test_helper import *
from sikuli import *

class ShortCutKeysTest():

    def NavigateDictionaryPane(self):
        find("DictionaryPane.png").click()
        assert exists("MainDictionaryMenu.png")
        

    def Findbox1(self):
        wait(1)
        find("MainDictionaryEntries.png").below(30).click()
        wait(1) 
        #type("f", Key.CTRL)
        keyDown(Key.CTRL)
        type("f")
        keyUp()
        assert exists("FindBox.png")
        type(Key.ESC)

    def Delete(self):
        wait(1)
        keyDown(Key.CTRL)
        type(Key.DELETE)
        keyUp(Key.CTRL)
        assert exists("Deletedialog-1.png")
        type(Key.ESC)

    def UndoRedo(self):
        wait(1)
        keyDown(Key.CTRL)
        type(Key.DELETE)
        keyUp(Key.CTRL)

        find("DeleteButton.png").click()
        wait("UndoEnabled.png", 5)
        type("z", Key.CTRL)
        wait(1)
        assert exists("UndoSuccess.png")
        find("UndoSuccess.png").highlight(1)
        type("y", Key.CTRL)
        wait(1)
        assert exists("UndoEnabled.png")
        find("UndoEnabled.png").highlight(1)

    def Findbox2(self):
        
        keyDown(Key.CTRL)
        type("f", Key.SHIFT)
        keyUp(Key.CTRL)
        assert exists("FindNextBox.png")
        keyDown(Key.ALT)
        keyDown(Key.F4)
        keyUp()
        wait(1)

    def NewEntryBox(self):

        #wait(10)
        type("e", Key.CTRL)
        assert exists("NewEntryBox.png")
        type(Key.ESC)
   
    def LeftandRight(self):
        wait(1)
        find(Pattern("Dictionaryview.png").exact()).click()
        find("Toolsmenu.png").click()
        find("Configure.png").click()
        find("RestoreDefaults.png").click()
        find("RestoreDefaultDialog.png")
        click("Yesbox.png")
        wait(Pattern("MainDictionaryEntries-1.png").targetOffset(-94,-1))
        find(Pattern("Dictionaryview.png").exact()).click()
        find("TextsandWords.png").click()
        wait(2)
        find("LexiconPane.png").click()
        wait(2)
    
        keyDown(Key.ALT)
        type(Key.LEFT)
        keyUp()
    
        if exists("TextPaneWait.png"):      
            assert exists(Pattern("RightArrow1.png").similar(0.90))
            find(Pattern("RightArrow1.png").similar(0.90)).highlight(1)
        else:
            print "Right Arrow is not enable it on Texts & Words pane"
            assert exists(Pattern("RightArrow1.png").similar(0.90))

        wait(2)
        keyDown(Key.ALT)
        type(Key.RIGHT)
        keyUp()
        wait(2)    
        if exists("LexiconPanewait.png"):
            assert exists(Pattern("LeftArrow1.png").similar(0.90))
            find(Pattern("LeftArrow1.png").similar(0.90)).highlight(1)
        else:
            assert exists(Pattern("LeftArrow1.png").similar(0.90))
            print "Left Arrow is not enable it on Lexicon pane"

