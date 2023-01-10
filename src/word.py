class Phonetic:

    def __init__(self, text, source):
        self.text = text
        self.source = source

class Meaning:

    def __init__(self, POS, definition):
        self.POS = POS
        self.definition = definition

class Word:

    phonetic = []
    meaning = []

    def __init__(self, term):
        self.term = term
        self.phonetic.clear()
        self.meaning.clear()

    def addPhonetic(self, newText, newSource  = "N/A"):
        self.phonetic.append(Phonetic(newText, newSource))

    def addMeaning(self, newPOS, newDefintion):
        self.meaning.append(Meaning(newPOS, newDefintion))