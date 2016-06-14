from app.Dictionary.dictionary import *
import os


testArticle = ['minutes', 'avec', 'agences', 'contrairement', 'aux', 'effectifs', 'des', 'spécialistes', 'qui', 'ont', 'le', 'vent', 'en', 'poupe', 'le', 'nombre', 'de', 'médecins', 'généralistes', 'baisse', 'presque', 'partout', 'en', 'ancecest', 'le', 'constat', 'préoccupant', 'dressé', 'par', 'le', 'conseil', 'national', 'de', 'ordre', 'des', 'traduire', 'par', 'la', 'perte', 'un', 'médecin', 'généraliste', 'sur', 'quatre', 'durant', 'la', 'période', 'alerte', 'organisme', 'représentant', 'la', 'profession', 'médicaleen', 'uselaugmentation', 'des', 'départs', 'à', 'la', 'retraite', 'entre', 'et', 'face', 'auxquels', 'les', 'médecins', 'généralistes', 'sont', 'les', 'premiers', 'touchésainsi', 'en', 'neuf', 'ans', 'leurs', 'effectifs', 'ont', 'diminué', 'de', 'pas', 'moins', 'de', 'départements', 'sont', 'concernés', 'en', 'particulier', 'paris', 'et', 'la', 'nièvre', 'devant', 'yonne', 'et', 'les', 'yvelines', 'a', 'lire', 'aussi', 'médecins', 'la', 'consultation', 'des', 'généralistes', 'pourrait', 'passer', 'à', 'euroset', 'alors', 'que', 'la', 'moyenne', 'pictwittercomndbsqxpihmotsclés']

testPrefix = ['mang', 'crev', 'pros', 'art', 'prep']

def testFindLemme():
    result = []
    for word in testArticle:
        result.append(findLemme(word))
    print(result)



def testFindLemmeFreq():
    result = []
    for word in testArticle:
        result.append(findLemmeFreq(word))
    print(result)

def testSuggestWord():
    print(os.getcwd())
    result = []
    for prefix in testPrefix:
        result.append(suggestWord(prefix))
    print(result)


testSuggestWord()
testFindLemme()
testFindLemmeFreq()

