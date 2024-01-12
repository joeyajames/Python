from collections import Counter


def solution(A):
    """
    A non-empty array A consisting of N integers is given.
    The unique number is the number that occurs exactly once in array A.

    You should find the first unique number in A. In other words,
    find the unique number with the lowest position in A.

    :param A: Non-empty array of N integers.
    :return: The first unique number in A. Returns -1 if no unique number found.
    """
    number_count = Counter(A)
    number_position = {num: pos for pos, num in enumerate(A)}

    for num, count in number_count.items():
        if count == 1:
            return num

    return -1


# Example usage:
A1 = [1, 4, 3, 3, 1, 2]
result1 = solution(A1)
print(result1)  # Output: 4

A2 = [6, 4, 4, 6]
result2 = solution(A2)
print(result2)  # Output: -1
