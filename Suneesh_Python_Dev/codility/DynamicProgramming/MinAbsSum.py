def solution(A):
    """
    Given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

    For a given array A, we are looking for such a sequence S that minimizes val(A,S):

    val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

    (Assume that the sum of zero elements equals zero.)

    For example, given array:
    A[0] = 1
    A[1] = 5
    A[2] = 2
    A[3] = -2
    the function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

    Assumptions:
    - N is an integer within the range [0..20,000];
    - Each element of array A is an integer within the range [−100..100].
    """

    N = len(A)

    # Initialize the minimum value of val(A, S) to infinity
    min_val = float('inf')

    # Iterate through all possible sequences S
    for i in range(2**N):
        sequence = []
        for j in range(N):
            # Extract the binary representation of i to form the sequence
            sequence.append(-1 if (i & (1 << j)) == 0 else 1)

        # Calculate the val(A, S) for the current sequence
        current_val = sum(A[k] * sequence[k] for k in range(N))

        # Update the minimum value
        min_val = min(min_val, abs(current_val))

    return min_val

# Example usage:
A = [1, 5, 2, -2]
result = solution(A)
print("Minimum value of val(A, S):", result)
