from kata.array_comparison import comp


def test_with_valid_input():
    a = [2, 5, 8]
    b = [25, 64, 4]
    assert comp(a, b)


def test_with_longer_valid_input():
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    assert comp(a, b)


def test_with_invalid_input():
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
    assert not comp(a, b)


def test_with_none_input():
    a = None
    b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
    assert not comp(a, b)
