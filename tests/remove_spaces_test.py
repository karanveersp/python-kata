from kata.remove_spaces import no_space


def test_1():
    expected = 'nospaces'
    test_input = 'n o   sp  a c   e s'
    assert no_space(test_input) == expected


def test_2():
    expected = 'thishasnospaceseither'
    test_input = 't h is ha s no spa  ce s e  i th  er      '
    assert no_space(test_input) == expected
