from collections import Counter


def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_lines(text):
    if not text:
        return 0

    return len(text.splitlines())


def most_common_word(text):
    words = text.lower().split()

    if not words:
        return None

    return Counter(words).most_common(1)[0][0]