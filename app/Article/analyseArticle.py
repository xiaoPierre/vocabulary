from app.BDD.connectBDD import *
from app.Dictionary.dictionary import *

art     = 'Alors que l’actrice était au téléphone avec une amie, ' \
          'Johnny Depp aurait ensuite crié dans l’appareil ' \
          '« appelle les flics ! ». L’acteur aurait toutefois ' \
          'pris la fuite juste avant l’arrivée de policiers au ' \
          'domicile du couple. Pour attester de cette violente ' \
          'altercation, Amber Heard et son avocate sont arrivées ' \
          'au tribunal de Los Angeles avec un dossier contenant ' \
          'des vidéos et des photos, dont ce cliché du visage ' \
          'meurtri de l’actrice.'

def analyseArticle(article):
    print(article)
    wordList = article.casefold().split(' ')
    print(wordList)
    freqList = []
    for item in wordList:
        newItem = item.replace('\xa0', '')
        if newItem.find("’") > 0:
            newItem = newItem[2:]
        for char in newItem:
            if not char.isalpha():
                newItem = newItem.replace(char, '')
        freqList.append(findLemmeFreq(newItem))
    return freqList

analyseArticle(art)

