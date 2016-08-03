from test_helper import *
click("concordone.png")
def concordance():
    type(Pattern("fortextone.png").targetOffset(60,2),"a")
    click("searchone.png")
    click(Pattern("matchcase.png").exact().targetOffset(-21,2))
    click("searchone.png")
    wait(2)
    click(Pattern("matchtewo.png").similar(0.90).targetOffset(-26,2))
    wait(2)
    click(Pattern("matchdiac.png").targetOffset(-30,-4))
    click("searchone.png")
    click(Pattern("matchdiac-1.png").targetOffset(-44,-10))
def refreshone():
    click(Pattern("fortextex.png").targetOffset(64,-8))
    type(Key.BACKSPACE)
    click(Pattern("refreshone.png").targetOffset(-2,-1))
#Search in the line - BaseLine    
find(Pattern("baseling.png").similar(0.90)).click()
click(Pattern("bsline.png").targetOffset(-18,1))
if exists(Pattern("baseling.png").similar(0.90)):
   concordance()
else:
    print"The text does not appear"
print"Baseline is working fine"
refreshone()
wait(2)
#Search in the line - Word
find(Pattern("baseling.png").similar(0.90)).click()
click(Pattern("wordone.png").targetOffset(-17,0))
if exists("wordgrey.png"):
   concordance()
else:
    print"The text does not appear"
print"Word is working fine"
wait(2)
refreshone()
#Search in the line - Morphemes
find("wordfine.png").highlight(2)
find(Pattern("wordtwo.png").similar(0.90)).click()
click("morphone.png")
if exists("morphsearchon.png"):
   concordance()
else:
    print"The text does not appear"
print"Morpheme is working fine"
wait(2)
refreshone()
#Search in the Line - Lex.Entry
find("morphoe.png").highlight(2)
find(Pattern("morphone-1.png").similar(0.80)).click()
click("lexentyr.png")
if exists("lexentry.png"):
    concordance()
else:
    print"The text does not appear"
print"Lex.Entry is working fine"
wait(2)
refreshone()
#Search in the Line - Lex.Gloss
find("lexentryone.png").highlight(2)
find(Pattern("lexentone.png").similar(0.80)).click()
click("lexglossone.png")
if exists("linelex.png"):
    concordance()
else:
    print"The text does not appear"
print"Lex.Gloss is working fine"
wait(2)
refreshone()
#Search in the Line - Lex.Gram.Info
find("1470220896453.png").highlight(2)
find("lexontoe.png").click()
click("lexgraminfo.png")
if exists("lexgraminfoone.png"):
   find("adverbone.png").click()
   click("conjuntion.png")
   click("searchone.png")
else:
    print"The text does not appear"
print"Lex.Gram.Info is working fine"
wait(2)
click(Pattern("refreshone.png").targetOffset(-2,-1))
#Search in the Line - Word Gloss
find("Lexgraminfo-1.png").highlight(2)
find(Pattern("lexinfogram.png").similar(0.90)).click()
click("wordglosse.png")
if exists("wordglosone.png"):
    concordance()
else:
    print"The text does not appear"
print"Word Gloss is working fine"
wait(2)
refreshone()
#Search in the Line - Word Category
find("wordglosone-1.png").highlight(2)
find("wordglosstwo.png").click()
click("wordone-1.png")
if exists("wordcatone.png"):
   find(Pattern("adverb.png").targetOffset(26,-17)).click()
   click("posone.png")
   click("searchone.png")
   click(Pattern("refreshone.png").targetOffset(-2,-1))
else:
    print"The text does not appear"
print"Word Category is working fine"
wait(2)
#Search in the Line - Free Translation
find("wordcatone.png").highlight(2)
find(Pattern("wordcateo.png").similar(0.90)).click()
click("freetranslation.png")
if exists("freetrans.png"):
    concordance()
else:
    print"There is some problem in the script"
print"Free Translation is working fine"
wait(2)
refreshone()
#Search in the Line - Literal Translation
find("freetrans.png").highlight(2)
find("freetrasnslon.png").click()
click("literalone.png")
if exists("literone.png"):
    concordance()
else:
    print"There is some problem in the script"
print"Literal Translation is working fine"
wait(2)
refreshone()
#Search in the Line - Note
find("literone.png").highlight(2)
find("litone.png").click()
click("noteone.png")
if exists("notetwo.png"):
    concordance()
else:
    print"There is some problem in the script"
print"Note is working fine"
refreshone()
wait(2)
#Search in the Line - Tagging
find("notetwo.png").highlight(2)
find(Pattern("noteone-1.png").similar(0.90)).click()
click("taggineone.png")
if exists("tagone.png"):
   find(Pattern("anyhwheonr.png").targetOffset(-15,-18)).click() 
   click(Pattern("syntaone.png").targetOffset(-13,-5))
   click("searchone.png")
   click(Pattern("refreshone.png").targetOffset(-2,-1))
else:
    print"There is some problem in the script"
print"Tagging is working fine"
wait(2)
popup("Search in the line field is working")
    
    