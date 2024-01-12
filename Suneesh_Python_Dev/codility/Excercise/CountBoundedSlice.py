def solution(K, A):
    N = len(A)
    result = 0
    right = 0
    left = 0
    max_value = A[0]
    min_value = A[0]

    while right < N:
        max_value = max(max_value, A[right])
        min_value = min(min_value, A[right])

        if max_value - min_value <= K:
            result += right - left + 1
            right += 1
        else:
            # Move the left pointer to the right and update max_value and min_value
            left += 1
            max_value = A[left]
            min_value = A[left]
            right = max(right, left)  # Ensure right is not behind left

        # Handle the case where the result exceeds 1,000,000,000
        if result > 1000000000:
            return 1000000000

    return result

# Example usage:
K = 2
A = [3, 5, 7, 6, 3]
result = solution(K, A)
print(result)  # Output: 9
