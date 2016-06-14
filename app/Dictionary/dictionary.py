from app.BDD.connectBDD import *
import pickle
import os

def findLemme(word):
    with connectBDD() as session:
        query = session.query(Word).filter(Word.ortho==word)
        if query.count() == 0:
            return ''
        for item in query:
            if item.lemme == item.ortho:
                return item.lemme
        return query[0].lemme


#optimise the database  time-consuming!!!!!!!
def findLemmeFreq(word):
    with connectBDD() as session:
        query = session.query(Word).filter(Word.ortho==word)
        if query.count() == 0:
            return 90000
        freqList = []
        for item in query:
            freqList.append(item.freqlemfilms)
        return max(freqList)

def suggestWord(prefix):
    print(os.getcwd())
    with open('dawgFile.dawg', 'rb') as dawgFile:
        dawgObj = pickle.load(dawgFile)
        words = dawgObj.keys(prefix)
        if len(words) > 6:
            return words[0:6]
        else:
            return dawgObj.keys(prefix)
