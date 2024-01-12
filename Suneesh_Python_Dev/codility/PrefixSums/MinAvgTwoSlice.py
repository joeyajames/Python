def solution(A):
    min_index = 0
    min_avg = (A[0] + A[1]) / 2.0  # Initial assumption with slice of size 2

    for i in range(2, len(A)):
        # Calculate average for slice of size 2
        avg2 = (A[i - 1] + A[i]) / 2.0
        if avg2 < min_avg:
            min_avg = avg2
            min_index = i - 1

        # Calculate average for slice of size 3
        avg3 = (A[i - 2] + A[i - 1] + A[i]) / 3.0
        if avg3 < min_avg:
            min_avg = avg3
            min_index = i - 2

    return min_index

# Example usage:
A = [4, 2, 2, 5, 1, 5, 8]
result = solution(A)
print(result)  # Output: 1
