import os
from pathlib import Path
from tabnanny import check
from typing import List
import re
import unicodedata
from urllib.request import urlretrieve


def _get_spanish_dictionary_words() -> List[str]:
    filename = "spanish.txt"
    # source of file
    # https://raw.githubusercontent.com/bitcoin/bips
    # /master/bip-0039/spanish.txt
    url = f"https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
    tmp_folder = os.getenv("TMP", "/tmp")
    local_filepath = Path(tmp_folder) / filename
    if not Path(local_filepath).exists():
        urlretrieve(url, local_filepath)
    return local_filepath.read_text().splitlines()


SPANISH_WORDS = _get_spanish_dictionary_words()

def convert_to_base(word):
    return unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('ascii')

def check_for_word_in_spanish(word):
    for w in SPANISH_WORDS:
        transformed_word = convert_to_base(w)
        if word == transformed_word:
            return w
    else:
        return word


def get_accentuated_sentence(
    text: str, words: List[str] = SPANISH_WORDS
) -> str:
    words_raw = re.split(r' ',text)
    final_sentence = []
    for word in words_raw:
        if re.match(r'\.+(\?)*', word):
            transformed_word = word
        elif ',' == word[-1:]:
            transformed_word = check_for_word_in_spanish(word)
        else:
            transformed_word = check_for_word_in_spanish(word)
        final_sentence.append(transformed_word)
    return ' '.join(final_sentence)

