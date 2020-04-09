from kata.square_digits import square_digits


def test_9119_gives_811181():
    expected = 811181
    assert square_digits(9119) == expected


def test_765_gives_493625():
    expected = 493625
    assert square_digits(765) == expected


def test_1_gives_1():
    assert square_digits(1) == 1


def test_0_gives_0():
    assert square_digits(0) == 0