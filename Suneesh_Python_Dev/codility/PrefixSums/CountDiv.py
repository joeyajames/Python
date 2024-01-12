def solution(A, B, K):
    divisible_count = 0

    # Iterate through the range [A..B]
    for i in range(A, B + 1):
        if i % K == 0:
            divisible_count += 1

    return divisible_count

# Example usage:
A = 6
B = 11
K = 2
result = solution(A, B, K)
print(result)
