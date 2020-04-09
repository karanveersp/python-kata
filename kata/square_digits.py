def square_digits(num):
    result = ""
    while num > 0:
        num, digit = divmod(num, 10)
        result = str(digit ** 2) + result

    if not result:
        result = 0

    return int(result)
