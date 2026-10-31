from analyzer import (
    count_characters,
    count_words,
    count_lines,
    most_common_word
)


def test_count_characters():
    assert count_characters("Hello World") == 11


def test_count_words():
    assert count_words("Python is easy") == 3


def test_count_lines():
    text = "First line\nSecond line\nThird line"
    assert count_lines(text) == 3


def test_count_lines_empty():
    assert count_lines("") == 0


def test_most_common_word():
    text = "python java python javascript python"
    assert most_common_word(text) == "python"


def test_most_common_word_case_insensitive():
    text = "Python python PYTHON"
    assert most_common_word(text) == "python"


def test_most_common_word_empty():
    assert most_common_word("") is None