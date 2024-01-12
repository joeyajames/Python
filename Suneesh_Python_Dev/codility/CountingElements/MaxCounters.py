def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_max = 0

    for operation in A:
        if 1 <= operation <= N:
            # Increase operation
            counters[operation - 1] = max(counters[operation - 1], last_max) + 1
            max_counter = max(max_counter, counters[operation - 1])
        elif operation == N + 1:
            # Max counter operation
            last_max = max_counter

    # Update counters for the remaining elements not affected by "max counter" operations
    for i in range(N):
        counters[i] = max(counters[i], last_max)

    return counters

# Example usage:
N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))  # Output: [3, 2, 2, 4, 2]
