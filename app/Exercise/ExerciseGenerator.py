import random
from difflib import SequenceMatcher

from app.Crawler.crawlImage import *
from app.Crawler.crawlWord import *
from app.Dictionary.dictionary import *
from app.Model.Exercise import *
from app.misc.etendu import etendu

# A tester!!!
class ExerciseGenerator:
    @staticmethod
    def proposeChoices(word):
        freq = findLemmeFreq(word)
        if freq > 500:
            k = 300
        elif freq > 100:
            k = 100
        else:
            k = 5
        with connectBDD() as session:
            wordModel = session.query(Word).filter(Word.ortho == word)
            words = []
            for item in wordModel:
                words.append(item)
            if (len(words) > 0):
                maxFreq = words[0].freqlemfilms
                maxWord = words[0]
                for item in words:
                    if item.freqlemfilms > maxFreq:
                        maxFreq = item.freqlemfilms
                        maxWord = item
                nature = maxWord.cgram
                proposition = session.query(Word).filter(Word.cgram == nature).filter(Word.freqlemfilms < (freq + k)).filter(
                    Word.freqlemfilms > (freq - k))
                lemmes = []
                for item in proposition:
                    lemmes.append(item.lemme)
                random.shuffle(lemmes)
                propositions = [lemmes[0], lemmes[1], lemmes[2], lemmes[3]]
                return propositions
            else:
                propositions = ['undefined', 'undefined', 'undefined', 'undefined']
                return propositions

    def generateExercise(self, word):
        pass


class BlankFillingExerciseGenerator(ExerciseGenerator):
    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def generateExercise(self, word):
        phrase = crawlPhrase(word)
        if phrase:
            wordList = phrase.split(' ')
            similarList = []
            for item in wordList:
                similarList.append(self.similar(item, word))
            valeurMax = max(similarList)
            position = similarList.index(valeurMax)
            wordList[position] = '_____'
            topic = ' '.join(wordList)
            choices = self.proposeChoices(word)
            ran = int(random.random() * 100) % 4
            choices[ran] = word
            return Exercise(topic, choices, ran)


class SynonymeExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word):
        synonyme = crawlSynonyme(word)
        if synonyme:
            topic = "Choisissez le mot qui a le même sens que '" + word + "'"
            choices = self.proposeChoices(word)
            ran = int(random.random() * 100) % 4
            choices[ran] = synonyme
            return Exercise(topic, choices, ran)


class AntonymeExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word):
        antonyme = crawlAntonyme(word)
        if antonyme:
            topic = "Choisissez le mot qui est le contraire de '" + word + "'"
            choices = self.proposeChoices(word)
            ran = int(random.random() * 100) % 4
            choices[ran] = antonyme
            return Exercise(topic, choices, ran)


class ImageExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word):
        topic = "Choisissez l'image qui correspond à '" + word + "'"
        choices = self.proposeChoices(word)
        ran = int(random.random() * 100) % 4
        choices[ran] = word
        images = []
        for choice in choices:
            choiceImage = crawlImage(choice)
            images.append(choiceImage)
        return Exercise(topic, images, ran)



class RandomExerciseGenerator(ExerciseGenerator):
    types = ['BlankFillingExerciseGenerator',
             'SynonymeExerciseGenerator',
             'AntonymeExerciseGenerator',
             'ImageExerciseGenerator']

    def generateExercise(self, word):
        while True:
            ran = int(random.random() * 100) % len(self.types)
            generator = globals()[self.types[ran]]()
            exercise = generator.generateExercise(word)
            if exercise:
                return exercise
            else:
                continue


#faut ecrire une classe d'adapteur!!!!!
class TotalRandomExerciseGenerator(RandomExerciseGenerator):
    def choisirMot(self):
        length = len(etendu)
        ran = int(random.random() * 1000) % (length-2)
        upper = etendu[ran]
        lower = etendu[ran + 1]
        with connectBDD() as session:
            words = session.query(Word).filter(Word.freqlemfilms >= lower) \
                .filter(Word.freqlemfilms <= upper)
            lemmes = []
            for word in words:
                lemmes.append(word.lemme)
        return random.choice(lemmes)

    def generateRandomExercise(self):
        word = self.choisirMot()
        return self.generateExercise(word)



#a = RandomExerciseGenerator()

#ERROR!!!!!!!!!
if __name__ == '__main__':

    b = RandomExerciseGenerator()
    exercise = b.generateExercise('content')
    print(exercise)
    #print(a.generateExercise('content'))


