
def count(str: str):
  """
  Given a string, return a dictionry containing characters as keys, and
  occurances as values.
  """
  # Create a list of tuples
  tuples = [(char, str.count(char)) for char in list(str)]

  # Create a dictionary from a list of tuples
  res = dict(tuples)
  
  # or single line dictionary comprehension
  # res = {k: v for k, v in [(c, str.count(c)) for c in list(str)]}
  return res

