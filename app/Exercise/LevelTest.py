from app.Exercise.ExerciseGenerator import *
from app.BDD.connectBDD import *
from app.misc.etendu import etendu
import random

def getLevelTests():
    wordTest = {}
    testGenerator = RandomExerciseGenerator()
    with connectBDD() as session:
        for i in range(len(etendu) - 1):
            upper = etendu[i]
            lower = etendu[i+1]
            words = session.query(Word).filter(Word.freqlemfilms>=lower)\
                .filter(Word.freqlemfilms<=upper)
            ran = int(random.random() * 20000) % words.count()
            ran2 = int(random.random() * 20000) % words.count()
            wordTest[i] = testGenerator.generateExercise(words[ran].lemme)
    return wordTest