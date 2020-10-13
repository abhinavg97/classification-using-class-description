import spacy
import unidecode


class TextProcessing:
    """
    Class to clean text
    """

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_text(self, text):
        text = self.unidecode(text)
        text = self.put_space_around_special_chars(text)
        text = self.remove_extra_whitespaces(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.lower_case(text)
        return text

    def remove_punctuation(self, text):
        text_tokens = self.nlp(text)
        tokens_without_sw = [word.text for word in text_tokens if not word.is_punct]
        return " ".join(tokens_without_sw)

    def remove_stopwords(self, text):
        text_tokens = self.nlp(text)
        tokens_without_sw = [word.text for word in text_tokens if not word.is_stop]
        return " ".join(tokens_without_sw)

    def put_space_around_special_chars(self, text):
        """
        Puts space around special chars like '[({$&*#@!'
        Args:
            text: text to be processed
        """

        chars = ['$', '?', '%', '@', '!', '#', '^', '*', '&', '"',
                 ':', ';', '/', '\\', ',', '+',
                 '(', ')', '[', ']', '{', '}', '<', '>']

        for char in chars:
            text = text.replace(char, ' '+char+' ')
        return text

    def remove_extra_whitespaces(self, text):
        """
        Removes extra whitespaces from the text
        Args:
            text: text to be processed
        """
        return text.strip()

    def unidecode(self, text):
        """
        unidecodes the text
        Args:
            text: text to be processed
        """
        return unidecode.unidecode(text.lower())

    def lower_case(self, text):
        """
        lower cases the text
        Args:
            text: text to be processed
        """
        return text.lower()


if __name__ == "__main__":

    processor = TextProcessing()

    text = "$10m is deep bot's net worth"

    text = processor.process_text(text)

    print(text)
