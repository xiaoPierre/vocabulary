from app.Crawler.crawlWord import *
words = ['minute', 'avec', 'agence', 'contrairement', 'aux', 'effectif', 'des', 'spécialiste', 'qui', 'avoir', 'le', 'vent', 'en', 'poupe', 'le', 'nombre', 'de', 'médecin', 'généraliste', 'baisse', 'presque', 'partout', 'en', '', 'le', 'constat', 'préoccupant', 'dressé', 'par', 'le', 'conseil', 'national', 'de', 'ordre', 'des', 'traduire', 'par', 'la', 'perte', 'un', 'médecin', 'généraliste', 'sur', 'quatre', 'durant', 'la', 'période', 'alerte', 'organisme', 'représentant', 'la', 'profession', '', '', 'des', 'départ', 'à', 'la', 'retraite', 'entre', 'et', 'face', 'auxquels', 'les', 'médecin', 'généraliste', 'être', 'les', 'premier', '', 'en', 'neuf', 'an', 'leurs', 'effectif', 'avoir', 'diminué', 'de', 'pas', 'moins', 'de', 'département', 'être', 'concerner', 'en', 'particulier', 'pari', 'et', 'la', '', 'devant', '', 'et', 'les', '', 'a', 'lire', 'aussi', 'médecin', 'la', 'consultation', 'des', 'généraliste', 'pouvoir', 'passer', 'à', '', 'alors', 'que', 'la', 'moyenne', '']
words2 = ['généraliste', 'partout', 'nombre', 'médecin', 'généraliste', 'baisse', 'presque', 'partout']

def testCrawlWord():
    result = []
    for word in words:
        content = crawlWord(word)
        print(content)
        result.append(crawlWord(word))

def testCrawlSynonyme():
    result = []
    for word in words:
        result.append(crawlSynonyme(word))
    print(result)

def testCrawlAntonyme():
    result = []
    for word in words:
        result.append(crawlAntonyme(word))
    print(result)

def testCrawlPhrase():
    result = []
    for word in words2:
        print(crawlPhrase(word))
        result.append(crawlPhrase(word))

#testCrawlWord()
#testCrawlSynonyme()
#testCrawlAntonyme()
testCrawlPhrase()
