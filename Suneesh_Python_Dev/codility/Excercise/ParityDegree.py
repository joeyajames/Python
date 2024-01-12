def solution(N):
    """
    A positive integer N is given. The goal is to find the highest power of 2 that divides N.
    In other words, we have to find the maximum K for which N modulo 2^K is 0.

    For example, given integer N = 24 the answer is 3, because 2^3 = 8 is the highest power of 2 that divides N.

    :param N: Positive integer to find the highest power of 2 for.
    :return: The highest power of 2 that divides N.
    """
    power_of_two = 0

    while N % 2 == 0:
        N //= 2
        power_of_two += 1

    return power_of_two


# Example usage:
N = 24
result = solution(N)
print(result)  # Output: 3
