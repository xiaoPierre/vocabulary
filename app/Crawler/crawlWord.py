import requests
from bs4 import BeautifulSoup
from app.Crawler.WordCrawled import *
def lookUpWord(word):
    natureListe = ['fr-nom', 'fr-nom-2', 'fr-adj', 'fr-adv',
                   'fr-verb', 'fr-interj', 'fr-flex-verb-1',
                   'fr-flex-verb-2', 'fr-adj-pos-1', 'fr-pronom-per-1']
    urlBase = r'https://fr.m.wiktionary.org/wiki/'
    url = urlBase + word
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    sectionFrancais = soup.find("div", id="mw-content-text", lang='fr')
    etymologie = sectionFrancais.find('dl').text
    natures = []
    for nature in natureListe:
        natureFound = lookNature(sectionFrancais, nature)
        if natureFound:
            natures.append(natureFound)
    return WordCrawled(etymologie, natures)

def lookNature(block, natureId):
    span = block.find('span', id=natureId)
    if not span:
        return
    natureNoun = fillWord(span)
    return natureNoun

def lookVerb(divBlock):
    wordFinal = {}
    span = divBlock.find("span", id="fr-verb")
    if not span:
        return
    h3block = span.parent.parent
    pblock1 = findNextPBlock(h3block)
    if (pblock1.name == 'p'):
        nature1 = pblock1.get_text()
        olblock1 = findNextSiblingNonEmpty(pblock1)
        word1 = []
        for item in olblock1.contents:
            if not item == '\n':
                definitions = {}
                stringList = item.get_text().split('\n')
                definitions['explanation'] = stringList[0]
                examples = []
                for i in range(1, len(stringList)):
                    examples.append(stringList[i])
                definitions['examples'] = examples
                word1.append(definitions)
        wordFinal[nature1] = word1


        pblock2 = findNextPBlock(olblock1)
        if (pblock2.name == 'p'):
            nature2 = pblock2.get_text()
            olblock2 = findNextSiblingNonEmpty(pblock2)
            word2=[]
            for item in olblock2.contents:
                if not item == '\n':
                    definitions = {}
                    stringList = item.get_text().split('\n')
                    definitions['explanation'] = stringList[0]
                    examples = []
                    for i in range(1, len(stringList)):
                        examples.append(stringList[i])
                    definitions['examples'] = examples
                    word2.append(definitions)
            wordFinal[nature2] = word2
    return wordFinal

def fillWord(span):
    h3block = span.parent.parent
    pblock = findNextBlock(h3block, 'p')
    if (pblock.name == 'p'):
        nature = pblock.get_text()
        olblock = findNextBlock(pblock, 'ol')
        definitions = []
        for item in olblock.contents:
            if not item == '\n':
                stringList = item.get_text().split('\n')
                explanation = stringList[0]
                examples = []
                for i in range(1, len(stringList)):
                    examples.append(stringList[i])
                definition = Definition(explanation, examples)
                definitions.append(definition)
        natureObj = Nature(nature, definitions)
        return natureObj

def findNextSiblingNonEmpty(node):
    temp = node
    while temp.nextSibling == '\n':
        temp = temp.nextSibling
    return temp.nextSibling

def findNextBlock(node, blockName):
    temp = node
    count = 0
    while findNextSiblingNonEmpty(temp).name != blockName:
        temp = findNextSiblingNonEmpty(temp)
        count += 1
        if count > 5:
            break
    return findNextSiblingNonEmpty(temp)

def crawlSynonyme(word):
    urlBase = 'http://www.crisco.unicaen.fr/des/synonymes/'
    url = urlBase + word
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    synonymesDIV = soup.find('div', id='synonymes')
    if synonymesDIV:
        ret = []
        synonymes = synonymesDIV.find_all('tr')
        for item in synonymes:
            ret.append(item.text)
        return ret
    else:
        return []

def crawlAntonyme(word):
    urlBase = 'http://www.antonyme.org/antonyme/'
    url = urlBase + word
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    conteneur = soup.find('div', id='conteneur')
    antonymeDIV = conteneur.find('ul', class_='synos')
    if antonymeDIV:
        ret = []
        antonymes = antonymeDIV.find_all('li')
        for item in antonymes:
            ret.append(item.text)
        return ret
    else:
        return []

if __name__ == '__main__':
    print(lookUpWord('crever_l’abcès'))
