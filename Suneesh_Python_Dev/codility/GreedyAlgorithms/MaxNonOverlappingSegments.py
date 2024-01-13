def solution(A, B):
    """
    Given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

    The segments are sorted by their ends, and two segments I and J are overlapping if they share at least one common point (A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J]).

    The goal is to find the size of a non-overlapping set containing the maximal number of segments.

    For example, given arrays A = [1, 3, 7, 9, 9] and B = [5, 6, 8, 9, 10], the function should return 3.

    Assumptions:
    - N is an integer within the range [0..30,000]
    - Each element of arrays A and B is an integer within the range [0..1,000,000,000]
    - A[I] ≤ B[I], for each I (0 ≤ I < N)
    - B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1)
    """

    if not A or not B:
        return 0

    non_overlapping_set_size = 1  # At least one segment is always part of the set
    current_end = B[0]  # Initialize with the end of the first segment

    for i in range(1, len(A)):
        if A[i] > current_end:
            # If the start of the next segment is greater than the current end, it doesn't overlap
            non_overlapping_set_size += 1
            current_end = B[i]  # Update the current end with the end of the non-overlapping segment

    return non_overlapping_set_size

# Example usage:
A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]
result = solution(A, B)
print("Size of Non-Overlapping Set:", result)
