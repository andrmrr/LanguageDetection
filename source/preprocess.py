import re
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd


def preprocess(sentences, labels):
    prep_sentences = []

    for sentence in sentences:
        # preprocess text
        sentence = sentence.lower()
        # sentence = remove_punctuation(sentence)
        sentence = ' '.join(sentence.split())
        prep_sentences.append(sentence)

    prep_sentences = pd.Series(prep_sentences)

    return prep_sentences, labels

def get_symbol_freq_by_family(sentence):
    symbol_families = {
        'Arabic': (0x0600, 0x06FF), 'Chinese': (0x4E00, 0x9FFF), 'Cyrillic': (0x0400, 0x04FF),
        'Turkish': (0x011E, 0x0131), 'Russian': (0x0400, 0x052F), 'English': (0x0020, 0x007F),
        'Spanish': (0x00C0, 0x024F), 'Korean': (0xAC00, 0xD7AF), 'Hindi': (0x0900, 0x097F),
        'French': (0x00C0, 0x024F), 'Thai': (0x0E00, 0x0E7F), 'Dutch': (0x0041, 0x024F),
        'Persian': (0x0600, 0x06FF), 'Pushto': (0x0620, 0x064A), 'Latin': (0x0041, 0x024F),
        'Estonian': (0x0100, 0x017F), 'Tamil': (0x0B80, 0x0BFF), 'Portuguese': (0x00C0, 0x024F),
        'Japanese': (0x3040, 0x30FF), 'Indonesian': (0x0041, 0x024F), 'Swedish': (0x0041, 0x024F),
        'Urdu': (0x0600, 0x06FF), 'Romanian': (0x0041, 0x024F)
    }

    abbreviations = {
        'Arabic': 'AR', 'Chinese': 'CN', 'Cyrillic': 'CY', 'Turkish': 'TR', 'Russian': 'RU',
        'English': 'EN', 'Spanish': 'ES', 'Korean': 'KR', 'Hindi': 'HI', 'French': 'FR',
        'Thai': 'TH', 'Dutch': 'NL', 'Persian': 'FA', 'Pushto': 'PS', 'Latin': 'LA',
        'Estonian': 'ET', 'Tamil': 'TA', 'Portuguese': 'PT', 'Japanese': 'JP', 'Indonesian': 'ID',
        'Swedish': 'SV', 'Urdu': 'UR', 'Romanian': 'RO'
    }

    total_symbols = len(sentence)
    family_freq = {abbr: 0 for abbr in abbreviations.values()}

    for char in sentence:
        for family, (start, end) in symbol_families.items():
            if start <= ord(char) <= end:
                family_freq[abbreviations[family]] += 1

    return [family_freq[abbr] / total_symbols if total_symbols > 0 else 0 for abbr in family_freq]


def remove_punctuation(sentence):
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    result = ""
    for char in sentence:
        if char not in punctuation_chars:
            result += char

    return result