def solution(K, A):
    """
    Given an integer K and a non-empty array A of N integers, returns the maximum number of ropes of length greater than or equal to K that can be created.

    For each I (0 ≤ I < N), the length of rope I on the line is A[I]. Two adjacent ropes can be tied together with a knot, and the length of the tied rope is the sum of lengths of both ropes. The resulting new rope can then be tied again.

    The goal is to tie the ropes in such a way that the number of ropes whose length is greater than or equal to K is maximal.

    For example, given K = 4 and array A such that:
    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 1
    A[5] = 1
    A[6] = 3
    The function should return 3.

    Assumptions:
    - N is an integer within the range [1..100,000]
    - K is an integer within the range [1..1,000,000,000]
    - Each element of array A is an integer within the range [1..1,000,000,000]
    """

    ropes_count = 0  # Initialize the count of ropes
    current_rope_length = 0  # Initialize the length of the current rope

    for rope_length in A:
        current_rope_length += rope_length  # Add the length of the current rope

        # If the length of the current rope becomes greater than or equal to K,
        # tie the current rope, reset the length, and increment the count
        if current_rope_length >= K:
            ropes_count += 1
            current_rope_length = 0

    return ropes_count

# Example usage:
K = 4
A = [1, 2, 3, 4, 1, 1, 3]
result = solution(K, A)
print("Maximum number of ropes:", result)
