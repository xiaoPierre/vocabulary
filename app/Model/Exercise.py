class Exercise:
    def __init__(self, topic, choices, answer):
        self.topic = topic
        self.choices = choices
        self.answer = answer
        self.isImageExo = False
        if self.choices[0].startswith('http'):
            self.isImageExo = True

    def __str__(self):
        strRes = self.topic + '\n'
        for choice in self.choices:
            strRes += choice + '\n'
        strRes += 'Bonne réponse:' + str(self.answer)
        return strRes


class ImageExercise(Exercise):
    pass
