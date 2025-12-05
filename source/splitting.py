
def split_ngrams(n, text):
    """Split a text into n-grams."""
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def split_trigrams(text):
    return split_ngrams(text, 3)