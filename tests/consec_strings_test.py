from kata.consec_strings import longest_consec

def test_consec_strings():
    expected = "abigailtheta"
    consec = ["zone", "abigail", "theta", "form", "libe", "zas", "theta",
              "abigail"]
    result = longest_consec(consec, 2)
    assert result == expected