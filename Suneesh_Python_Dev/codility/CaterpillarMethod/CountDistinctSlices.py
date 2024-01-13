def solution(M, A):
    """
    Given an integer M and a non-empty array A consisting of N integers,
    returns the number of distinct slices.

    A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
    The slice consists of the elements A[P], A[P + 1], ..., A[Q].
    A distinct slice is a slice consisting of only unique numbers. That is,
    no individual number occurs more than once in the slice.

    If the number of distinct slices is greater than 1,000,000,000,
    the function returns 1,000,000,000.

    Assumptions:
    - N is an integer within the range [1..100,000];
    - M is an integer within the range [0..100,000];
    - Each element of array A is an integer within the range [0..M].
    """

    # Initialize variables
    total_slices = 0
    last_occurrence = [-1] * (M + 1)
    front_pointer = 0

    # Iterate through the array using a back pointer
    for back_pointer in range(len(A)):
        # Move the front pointer to the maximum of its current position and the last occurrence of the current element
        front_pointer = max(front_pointer, last_occurrence[A[back_pointer]] + 1)

        # Update the total slices by adding the number of slices ending at the current position
        total_slices += (back_pointer - front_pointer + 1)

        # If the total slices exceed the limit, return the maximum limit
        if total_slices > 1000000000:
            return 1000000000

        # Update the last occurrence of the current element
        last_occurrence[A[back_pointer]] = back_pointer

    return total_slices

# Example usage:
M = 6
A = [3, 4, 5, 5, 2]
result = solution(M, A)
print("Number of distinct slices:", result)
