from app.Dictionary.dictionary import *
from app.Crawler.crawlArticle import *
from app.Exercise.LevelTest import etendu
art = crawlArticle('sante').content

def analyseArticle(article):
    wordList = article.casefold().split(' ')
    freqList = []
    newList = []
    for item in wordList:
        newItem = item.replace('\xa0', '')
        if newItem.find("’") > 0:
            newItem = newItem[2:]
        for char in newItem:
            if not char.isalpha():
                newItem = newItem.replace(char, '')
        newList.append(newItem)
        freq = findLemmeFreq(newItem)
        i = 0
        while freq < etendu[i]:
            i+=1
            if i >= len(etendu) - 1:
                i = 99
                break
        freqList.append({item : i})
    return freqList

