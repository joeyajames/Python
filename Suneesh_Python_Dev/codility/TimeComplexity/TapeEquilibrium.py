def solution(A):
    total_sum = sum(A)
    min_difference = float('inf')
    left_sum = 0

    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        difference = abs(left_sum - right_sum)
        min_difference = min(min_difference, difference)

    return min_difference

# Example usage:
A = [3, 1, 2,5, 4, 3,7,3]
print(solution(A))  # Output: 1
