from src.corpus.ja import JapaneseCorpus
from src.normalizer.ja import JapaneseNormalizer
from src.summarizer import Summarizer


class SumyActionProcessor:
    def __init__(self, text):
        self.__text: str = text
        self.__corpus_maker: JapaneseCorpus = JapaneseCorpus()

    def run(self):
        normalized = JapaneseNormalizer.normalize(self.__text)
        sentences = self.__corpus_maker.make_sentences(normalized)
        corpus = self.__corpus_maker.make_corpus(sentences)
        return Summarizer(sentences, corpus).summarize()
