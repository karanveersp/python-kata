def comp(a1, a2):
    """Compares a1 to a2 with the criteria
    that all values in a2 should be squares of values in a1"""
    try:
        # return sorted(x * x for x in a1) == sorted(a2)
        for num in a1:
            square = num ** 2
            if square in a2:
                a2.remove(square)
            else:
                return False
        return True
    except Exception:
        return False
