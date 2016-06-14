from app.Exercise.ExerciseGenerator import *
words = ['généraliste', 'partout', 'nombre', 'médecin', 'généraliste', 'baisse', 'presque', 'partout']
words2 = ['généraliste', 'généraliste','généraliste','généraliste','généraliste','généraliste']
def testRandomExerciseGenerator():
    a = RandomExerciseGenerator()
    for word in words2:
        print(a.generateExercise(word))

testRandomExerciseGenerator()