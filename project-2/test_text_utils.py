from text_utils import is_palindrome, reverse_string


def test_is_palindrome_true():
    assert is_palindrome("Kasur ini rusak") is True
    assert is_palindrome("Katak") is True


def test_is_palindrome_false():
    assert is_palindrome("Halo dunia") is False
    assert is_palindrome("Python") is False


def test_reverse_string():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("CI/CD") == "DC/IC"