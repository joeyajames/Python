def solution(A):
    n = len(A)
    unique_elements = set()

    for num in A:
        if not 1 <= num <= n or num in unique_elements:
            return 0  # Not a permutation

        unique_elements.add(num)

    return 1  # A is a permutation

def solution_arithmetic(A):
    n = len(A)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(A)
    unique_elements = set(A)

    if len(unique_elements) == n and actual_sum == expected_sum:
        return 1  # A is a permutation
    else:
        return 0  # A is not a permutation
# Example usage:
A1 = [4, 1, 3, 2]
print(solution(A1))  # Output: 1

A2 = [6, 1, 3]
print(solution(A2))  # Output: 0
