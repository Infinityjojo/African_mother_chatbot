import re

STOP_WORDS = {
    "the", "is", "am", "are", "i", "you", "me", "my", "to",
    "and", "a", "of", "in", "on", "for", "it", "this", "that"
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOP_WORDS]
    return set(tokens)
