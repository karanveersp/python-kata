from kata.isogram import is_isogram


def test_isogram_returns_true():
    test_input = "isogram"
    assert is_isogram(test_input)


def test_empty_string_returns_true():
    test_input = ""
    assert is_isogram(test_input)


def test_ignores_case_repeat_returns_false():
    test_input = "moOse"
    assert not is_isogram(test_input)


def test_repeat_returns_false():
    test_input = "aba"
    assert not is_isogram(test_input)
