def anagrams(word, words):
    """Filters words list for anagrams of word and returns the list"""
    return [item for item in words if sorted(item) == sorted(word)]

    # orignal solution
    # anagrams = []

    # words = [value for value in words if len(value) == len(word)]
    # letters = list(word)

    # for value in words:
    #     current_word = value
    #     for letter in letters:
    #         value = value.replace(letter, "", 1)
    #     if not len(value):
    #         anagrams.append(current_word)
    # return anagrams
