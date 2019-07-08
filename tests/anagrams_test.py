from kata.anagrams import anagrams


def test_1():
    expected = ["baab"]
    values = ["bbaab", "baab"]
    assert anagrams("abba", values) == expected


def test_2():
    expected = ["carer", "racer"]
    values = ['crazer', 'carer', 'racar', 'caers', 'racer']
    assert anagrams('racer', values) == expected
