def longest_consec(strarr, k):
    """Returns first longest string made of k consecutive strings in strarr"""
    n = len(strarr)
    longest = ""

    if k > 0 and k <= n:
        for i in range(n - k + 1):
            current = "".join(strarr[i: i + k])
            if len(current) > len(longest):
                longest = current

    return longest


if __name__ == "__main__":
    expected = "abigailtheta"
    consec = ["zone", "abigail", "theta", "form", "libe", "zas", "theta",
              "abigail"]
    result = longest_consec(consec, 2)
    print(result == expected)
