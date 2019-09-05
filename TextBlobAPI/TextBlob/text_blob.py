from textblob import TextBlob
from langdetect import detect
from nltk.corpus import stopwords


class TutorialTextBlob:
    def __init__(self, text):
        self.text = text.lower()
        self.textblob = TextBlob(self.text)
        try:
            self.source_lang = detect(self.text)
        except (TimeoutError, ConnectionError):
            print("Didn't detect the language")

        if self.source_lang == 'en':
            lista = [word for word in self.textblob.words if word not in stopwords.words('english')]
            tekst = ' '.join(lista)
            self.textblob = TextBlob(tekst)
        else:
            lista = [word for word in self.textblob.words if word not in stopwords.words('arabic')]
            tekst = ' '.join(lista)
            self.textblob = TextBlob(tekst)

        self.words = self.textblob.words
        self.sentences = self.textblob.sentences
        self.part_of_speech = self.textblob.tags
        self.nouns = self.textblob.noun_phrases

    def translate(self, target_lang='en'):
        return self.textblob.translate(from_lang=self.source_lang, to=target_lang)

    def lemmatize(self):
        return self.words.lemmatize()

    def n_grams(self, grams=3):
        return self.textblob.ngrams(grams)

    def text_correction(self):
        return self.textblob.correct()
