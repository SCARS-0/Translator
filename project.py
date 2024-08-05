from tabulate import tabulate
from googletrans import Translator, LANGUAGES


class TranslateClass(object):
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
        self.Trans = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        try:
            translated = self.Trans.translate(self.word, dest=self.lang).text
        except Exception as e:
            translated = f"Translation Error: {str(e)}"

        language_name = LANGUAGES.get(self.lang, "Unknown Language").capitalize()

        data = [
            ["Language:", "Word/Sentence"],
            ["English", self.word],
            [language_name, str(translated)],
        ]
        table = str(tabulate(data, headers="firstrow", tablefmt="grid"))
        return table


if __name__ == "__main__":
    translate = input("Enter Word/Sentence: ")
    lang = input(
        "which language you want it to translate to?\n1.'hi' for hindi\n\n2.'kn' for kanada\n\n3.'ar' for arabic\n\n4.'de' for german\n\n5.'it' for italian\nChoice: "
    )
    language = lang
    print(TranslateClass(translate, language))
