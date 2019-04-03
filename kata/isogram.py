def is_isogram(string):
    """An isogram is a word with no repeating letters, case insensitive.
    This method checks whether the input string is an isogram"""
    # result = True
    # string_set = set()
    # for s in string:
    #     string_set.add(s.lower())

    # if len(string_set) != len(string):
    #     result = False
    # return result
    return len(string) == len(set(string.lower()))


if __name__ == "__main__":
    testVal = 'tsil'
    print(is_isogram(testVal))
