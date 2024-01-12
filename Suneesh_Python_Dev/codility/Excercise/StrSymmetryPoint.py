def solution(S):
    """
    Given a string S, returns the index (counting from 0) of a character
    such that the part of the string to the left of that character is a
    reversal of the part of the string to its right. The function should
    return −1 if no such index exists.

    Note: reversing an empty string (i.e. a string whose length is zero)
    gives an empty string.

    :param S: The input string.
    :return: The index of the character meeting the specified condition,
             or -1 if no such index exists.
    """
    n = len(S)

    for i in range(n):
        left = S[:i]
        right = S[i + 1:]

        if left == right[::-1]:
            return i

    return -1


# Example usage:
result1 = solution("racecar")
print(result1)  # Output: 3

result2 = solution("x")
print(result2)  # Output: 0
