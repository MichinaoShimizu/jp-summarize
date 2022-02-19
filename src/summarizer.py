from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words


class Summarizer:
    def __init__(self, sentences, corpus):
        self.__sentences = sentences
        self.__corpus = corpus

    def summarize(self):
        lang = "japanese"
        summarizer = TextRankSummarizer()
        summarizer.stop_words = get_stop_words(lang)
        parser = PlaintextParser.from_string(" ".join(self.__corpus), Tokenizer(lang))
        summary = summarizer(parser.document, 3)
        return [str(self.__sentences[self.__corpus.index(str(s))]) for s in summary]
