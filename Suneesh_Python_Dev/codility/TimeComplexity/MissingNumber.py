def solution_list(A):
    element_set = set(A)

    N = len(A) + 1

    for i in range(1, N + 1):
        if i not in element_set:
            return i

def solution(A):
    N = len(A) + 1
    expected_sum = (N * (N + 1)) // 2
    actual_sum = sum(A)
    missing_element = expected_sum - actual_sum
    return missing_element

# Example usage:
A = [2, 3, 1, 5]
print(solution(A))  # Output: 4
