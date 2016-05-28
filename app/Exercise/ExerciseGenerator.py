from app.Crawler.crawlWord import *
from app.Crawler.crawlImage import *
from app.Model.Word import *
from app.Exercise.Exercise import *
import random, re
from difflib import SequenceMatcher

def proposeChoices(word, freq):
    engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
    Session = sessionmaker(bind=engine)
    session = Session()
    wordModel = session.query(Word).filter(Word.ortho==word)
    words = []
    for item in wordModel:
        words.append(item)
    assert(len(words) > 0)
    maxFreq = 0
    maxWord = None
    for item in words:
        if item.freqfilms > maxFreq:
            maxFreq = item.freqfilms
            maxWord = item
    nature = maxWord.cgram
    proposition = session.query(Word).filter(Word.cgram==nature).filter(Word.freqlemfilms < (freq + 3)).filter(Word.freqlemfilms > (freq - 3))
    lemmes = set()
    for item in proposition:
        lemmes.add(item.lemme)
    propositions = []
    propositions.append(lemmes.pop())
    propositions.append(lemmes.pop())
    propositions.append(lemmes.pop())
    propositions.append(lemmes.pop())
    session.close()
    return propositions

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def blankFillingExo(word, freq):
    phrase = crawlPhrase(word)
    if phrase:
        wordList = phrase.split(' ')
        pattern = re.compile(r'^[A-Za-zàéèëêïîôùûçœ]+')
        '''
        resultList = []
        for item in wordList:
            if pattern.match(item):
                if item.find('\'') > 0 or item.find('’') > 0:
                    item = item[2:]
                if item.find('.') > 0 or item.find(',') > 0 or item.find(';') > 0:
                    item = item[0:-1]
                resultList.append(item.lower())
        print(resultList)
        '''
        similarList = []
        for item in wordList:
            similarList.append(similar(item, word))
        valeurMax = max(similarList)
        position = similarList.index(valeurMax)
        wordList[position] = '_____'
        topic = ' '.join(wordList)
        choices = proposeChoices(word, freq)
        ran = int(random.random() * 100) % 4
        choices[ran] = word
        return Exercise(topic, choices, ran)




def synonymeExo(word, freq):
    synonyme = crawlSynonyme(word)
    phrase = crawlPhrase(word)
    if synonyme:
        topic = phrase + '\n' + 'dans cette phrase, le mot ' + word + ' peut être remplacé par: '
        choices = proposeChoices(word, freq)
        ran = int(random.random() * 100) % 4
        choices[ran] = synonyme
        return Exercise(topic, choices, ran)



def antonymeExo(word, freq):
    antonyme = crawlAntonyme(word)
    phrase = crawlPhrase(word)
    if antonyme:
        topic = phrase + '\n' + 'dans cette phrase, le mot ' + word + " est à l'opposé de: "
        choices = proposeChoices(word, freq)
        ran = int(random.random() * 100) % 4
        choices[ran] = antonyme
        return Exercise(topic, choices, ran)


def imageExo(word, freq):
    topic = "Choisir l'image qui correspond à " + word
    choices = proposeChoices(word, freq)
    ran = int(random.random() * 100) % 4
    choices[ran] = word
    images = []
    for choice in choices:
        choiceImage = crawlImage(choice)
        images.append(choiceImage)
    return Exercise(topic, images, ran)


def prononciationExo(word):
    pass




print(blankFillingExo('lumière', 1000))