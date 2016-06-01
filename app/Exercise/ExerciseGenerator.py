from app.Crawler.crawlWord import *
from app.Crawler.crawlImage import *
from app.BDD.connectBDD import *
from difflib import SequenceMatcher
from app.Model.Word import *
from app.Exercise.Exercise import *
import random


class ExerciseGenerator:
    @staticmethod
    def proposeChoices(word, freq):
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
            assert (len(words) > 0)
            maxFreq = 0
            maxWord = None
            for item in words:
                if item.freqfilms > maxFreq:
                    maxFreq = item.freqfilms
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

    def generateExercise(self, word, freq):
        pass


class BlankFillingExerciseGenerator(ExerciseGenerator):
    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def generateExercise(self, word, freq):
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
            choices = self.proposeChoices(word, freq)
            ran = int(random.random() * 100) % 4
            choices[ran] = word
            return Exercise(topic, choices, ran)


class SynonymeExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word, freq):
        synonyme = crawlSynonyme(word)
        if synonyme:
            topic = "Choisissez le mot qui a le même sens que " + word
            choices = self.proposeChoices(word, freq)
            ran = int(random.random() * 100) % 4
            choices[ran] = synonyme
            return Exercise(topic, choices, ran)


class AntonymeExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word, freq):
        antonyme = crawlAntonyme(word)
        if antonyme:
            topic = "Choisissez le mot qui a le sens opposé que " + word
            choices = self.proposeChoices(word, freq)
            ran = int(random.random() * 100) % 4
            choices[ran] = antonyme
            return Exercise(topic, choices, ran)


class ImageExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word, freq):
        topic = "Choisissez l'image qui correspond à " + word
        choices = self.proposeChoices(word, freq)
        ran = int(random.random() * 100) % 4
        choices[ran] = word
        images = []
        for choice in choices:
            choiceImage = crawlImage(choice)
            images.append(choiceImage)
        return Exercise(topic, images, ran)


class PrononciationExerciseGenerator(ExerciseGenerator):
    def generateExercise(self, word, freq):
        pass


class RandomExerciseGenerator(ExerciseGenerator):
    types = ['BlankFillingExerciseGenerator',
             'SynonymeExerciseGenerator',
             'AntonymeExerciseGenerator',
             'ImageExerciseGenerator']

    def generateExercise(self, word, freq):
        ran = int(random.random() * 100) % len(self.types)
        generator = globals()[self.types[ran]]()
        return generator.generateExercise(word, freq)

'''
a = RandomExerciseGenerator()

#ERROR!!!!!!!!!
print(a.generateExercise('content', 1000))

print(a.generateExercise('content', 50))

'''