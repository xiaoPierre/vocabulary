import requests
from bs4 import BeautifulSoup

def lookUpWord(word):
    result = {}
    urlBase = r'https://fr.m.wiktionary.org/wiki/'
    url = urlBase + word
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    sectionFrancais = soup.find("div", class_="mf-section-1")
    if not sectionFrancais:
        return result
    #etymologie = sectionFrancais.find('dl').get_text()
    #result['etymologie'] = etymologie
    result['verb'] = lookVerb(sectionFrancais)
    result['noun'] = lookNoun(sectionFrancais)
    result['noun2'] = lookNoun2(sectionFrancais)
    result['adj'] = lookAdj(sectionFrancais)
    result['adv'] = lookAdv(sectionFrancais)
    result['interj'] = lookInterj(sectionFrancais)
    return result



def lookNoun(block):
    wordFinal = {}
    span = block.find('span', id='fr-nom')
    if not span:
        return
    nature1, word1 = fillWord(span)
    wordFinal[nature1] = word1
    return wordFinal

def lookNoun2(block):
    wordFinal = {}
    span = block.find('span', id='fr-nom-2')
    if not span:
        return
    nature1, word1 = fillWord(span)
    wordFinal[nature1] = word1
    return wordFinal

def lookAdj(divBlock):
    wordFinal = {}
    span = divBlock.find('span', id='fr-adj')
    if not span:
        return
    nature1, word1 = fillWord(span)
    wordFinal[nature1] = word1
    return wordFinal

def lookAdv(divBlock):
    wordFinal = {}
    span = divBlock.find('span', id='fr-adv')
    if not span:
        return
    nature1, word1 = fillWord(span)
    wordFinal[nature1] = word1
    return wordFinal

def lookInterj(divBlock):
    wordFinal = {}
    span = divBlock.find('span', id='fr-interj')
    if not span:
        return
    nature1, word1 = fillWord(span)
    wordFinal[nature1] = word1
    return wordFinal


def lookVerb(divBlock):
    wordFinal = {}
    span = divBlock.find("span", id="fr-verb")
    if not span:
        return
    h3block = span.parent.parent
    pblock1 = findNextPBlock(h3block)
    if (pblock1.name == 'p'):
        nature1 = pblock1.get_text()
        olblock1 = findNextSiblinNonEmpty(pblock1)
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
            olblock2 = findNextSiblinNonEmpty(pblock2)
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
    pblock1 = findNextPBlock(h3block)
    if (pblock1.name == 'p'):
        nature1 = pblock1.get_text()
        olblock1 = findNextSiblinNonEmpty(pblock1)
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
        return nature1, word1

def findNextSiblinNonEmpty(node):
    temp = node
    while temp.nextSibling == '\n':
        temp = temp.nextSibling
    return temp.nextSibling

def findNextPBlock(node):
    temp = node
    count = 0
    while findNextSiblinNonEmpty(temp).name != 'p':
        temp = findNextSiblinNonEmpty(temp)
        count=count+1
        if (count > 3):
            break
    return findNextSiblinNonEmpty(temp)

def dictToWord():
    a = {'postuler intransitif 1er groupe (conjugaison)': [{'examples': [], 'explanation': '(Justice) Se dit d’un avoué qui occupe pour une partie, et qui fait tous les actes de procédure nécessaires à l’instruction de l’affaire.'}], 'postuler \\pɔs.ty.le\\ transitif 1er groupe (conjugaison)': [{'examples': ['Postuler un emploi, une place.', 'Postuler l’admission dans une maison religieuse.', ''], 'explanation': 'Solliciter, faire des démarches pour obtenir quelque chose.'}, {'examples': ['Ce chapitre postule un tel pour évêque.', 'Tel évêque a été postulé pour tel archevêché.', ''], 'explanation': '(Vieilli) Il se dit aussi en matière ecclésiastique.'}, {'examples': ['Postuler la bonne volonté (traduction littérale de la recommandation anglaise assume good faith)', ''], 'explanation': 'Poser comme postulat.'}]}
    print(len(a.keys()))
    for key in a.keys():
        print(key)
        for item in a[key]:
            print(item['explanation'])
            print(item['examples'])


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
    print(crawlAntonyme('mangerais'))
