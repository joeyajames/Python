def solution(A):
    N = len(A)

    # Edge case: if the array has less than 4 elements, no double slice is possible
    if N < 4:
        return 0

    # Initialize arrays to store the maximum sum ending at each index and starting at each index
    max_ending = [0] * N
    max_starting = [0] * N

    # Calculate the maximum sum ending at each index
    for i in range(1, N - 1):
        max_ending[i] = max(0, max_ending[i - 1] + A[i])

    # Calculate the maximum sum starting at each index
    for i in range(N - 2, 0, -1):
        max_starting[i] = max(0, max_starting[i + 1] + A[i])

    # Initialize the maximum double slice sum to 0
    max_double_slice = 0

    # Iterate through each possible ending position of the left slice
    for i in range(1, N - 1):
        # Calculate the total double slice sum for the current ending position
        double_slice_sum = max_ending[i - 1] + max_starting[i + 1]

        # Update the maximum double slice sum if the current sum is greater
        max_double_slice = max(max_double_slice, double_slice_sum)

    return max_double_slice

# Example usage:
array_A = [3, 2, 6, -1, 4, 5, -1, 2]
result = solution(array_A)
print("Maximal Sum of any Double Slice:", result)
