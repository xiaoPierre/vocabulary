class WordCrawled:

    def __init__(self, etymonogie, natures):
        self.etymonogie = etymonogie
        self.natures = natures


    def __str__(self):
        strRes = self.etymonogie
        for nature in self.natures:
            strRes = strRes + nature.__str__() + '\n'
        return strRes
class Nature:

    def __init__(self, categorie, definitions):
        self.categorie = categorie
        self.definitions = definitions

    def __str__(self):
        strRes = self.categorie + '\n'
        for item in self.definitions:
            strRes = strRes + '\t' + item.__str__() + '\n'
        return strRes


class Definition:
    def __init__(self, definition, exemples):
        self.definition = definition
        self.exemples = exemples


    def __str__(self):
        strRes = self.definition + '\n'
        for item in self.exemples:
            strRes = strRes + '\t\t' + item + '\n'
        return strRes