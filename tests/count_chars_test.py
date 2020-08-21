from kata.count_chars import count

def test_works_with_aba():
  assert(count("aba") == {"a": 2, "b": 1})

def test_works_with_1223334444():
  assert(count("1223334444") == {"1": 1, "2": 2, "3": 3, "4": 4})

def test_works_with_asdf():
  assert(count("asdf") == {"a": 1, "s": 1, "d": 1, "f": 1})

def test_works_with_empty_str():
  assert(count("") == {})