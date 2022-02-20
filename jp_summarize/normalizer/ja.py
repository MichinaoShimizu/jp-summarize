import re
from typing import List

import mojimoji
import neologdn


class JapaneseNormalizer:
    @staticmethod
    def normalize(text: str) -> List[str]:
        text = re.sub(r"\n", "", text)
        text = re.sub(r"\r", "", text)
        text = re.sub(r"\s", "", text)
        text = re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+", "", text)
        text = re.sub(r"[!-~]", "", text)
        text = re.sub(r"[︰-＠]", "", text)
        text = text.lower()
        text = mojimoji.zen_to_han(text, kana=True)
        text = mojimoji.han_to_zen(text, digit=False, ascii=False)
        text = text.strip()
        text = neologdn.normalize(text)
        return text.split("。")
