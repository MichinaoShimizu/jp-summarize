from typing import List

from janome.analyzer import Analyzer
from janome.charfilter import RegexReplaceCharFilter, UnicodeNormalizeCharFilter
from janome.tokenfilter import ExtractAttributeFilter, POSKeepFilter
from janome.tokenizer import Tokenizer as JanomeTokenizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer

from src.normalizer.ja import JapaneseNormalizer


class SumyActionProcessor:
    def __init__(self, text: str):
        self.__text: str = text
        self.__analyzer = Analyzer(
            char_filters=[
                UnicodeNormalizeCharFilter(),
                RegexReplaceCharFilter(r"[(\)「」、。]", " "),
            ],
            tokenizer=JanomeTokenizer(),
            token_filters=[
                POSKeepFilter(["名詞", "形容詞", "副詞", "動詞"]),
                ExtractAttributeFilter("base_form"),
            ],
        )

    def run(self) -> List[str]:
        normalized: List[str] = JapaneseNormalizer.normalize(self.__text)
        corpus = [" ".join(self.__analyzer.analyze(s)) + "。" for s in normalized]
        parser = PlaintextParser.from_string("".join(corpus), Tokenizer("japanese"))
        summarizer = LexRankSummarizer()
        summarizer.stop_words = [" "]
        summary = summarizer(parser.document, int(len(corpus) / 10 * 3))
        return [normalized[corpus.index(s.__str__())] for s in summary]
