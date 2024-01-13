def solution(A):
    """
    Given an array A consisting of N integers, returns the number of triangular triplets.

    A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides
    of lengths A[P], A[Q], and A[R].

    Assumptions:
    - N is an integer within the range [0..1,000];
    - Each element of array A is an integer within the range [1..1,000,000,000].
    """

    # Sort the array in non-decreasing order
    A.sort()

    # Initialize the count of triangular triplets
    count_triplets = 0

    # Iterate through the array from right to left
    for r in range(len(A) - 1, 1, -1):
        # Initialize pointers for the other two sides of the triangle
        p = 0
        q = r - 1

        # Check for triangular triplets
        while p < q:
            if A[p] + A[q] > A[r]:
                # If a triplet is found, all pairs (p, q) in between form valid triangles
                count_triplets += q - p
                # Move the q pointer to check for more triplets
                q -= 1
            else:
                # If the condition is not met, move the p pointer to increase the sum
                p += 1

    return count_triplets

# Example usage:
A = [10, 2, 5, 1, 8, 12]
result = solution(A)
print("Number of triangular triplets:", result)
