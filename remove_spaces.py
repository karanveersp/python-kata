def no_space(s):
    """Returns string with all spaces removed from input s"""
    return s.replace(' ', '')


if __name__ == "__main__":
    expected = 'nospace'
    testval = 'no spa c e '
    print(no_space(testval) == expected)
