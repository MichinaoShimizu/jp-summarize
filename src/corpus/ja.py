import spacy
from janome.analyzer import Analyzer
from janome.charfilter import RegexReplaceCharFilter, UnicodeNormalizeCharFilter
from janome.tokenfilter import ExtractAttributeFilter


class JapaneseCorpus:
    def __init__(self):
        self.__nlp = spacy.load("ja_ginza")
        self.__analyzer = Analyzer(
            char_filters=[
                UnicodeNormalizeCharFilter(),
                RegexReplaceCharFilter(r"[(\)「」、。]", " "),
            ],
            token_filters=[
                ExtractAttributeFilter("base_form"),
            ],
        )

    def make_sentences(self, sentences):
        return self.__nlp(sentences).sents

    def make_corpus(self, sentences):
        return ["".join(self.__analyzer.analyze(str(s))) + "。" for s in sentences]
