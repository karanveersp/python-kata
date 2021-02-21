def sum_of_multiples_of_3_5(target: int) -> int:
    """original"""
    return sum([m for m in range(1, target) if m % 3 == 0 or m % 5 == 0])


def faster_sum_of_multiples_of_3_5(target: int) -> int:
    """
    Using 1+2+3+...+n = 1/2 * n * (n+1)
    and 3 * (1+2+3...+333) + 5 (1+2+3...+199) - 15(1+2+3...+66)
    since multiples of 15 are duplicated in both 3 and 5,
    we get the sum of multiples of 3 and 5.
    """

    def sum_divisible_by(n: int) -> int:
        p = (target - 1) // n  # -1 because target itself not included
        return n * (p * (p + 1)) // 2

    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
