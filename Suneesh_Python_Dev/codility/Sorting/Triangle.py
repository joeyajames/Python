def solution(A):
    """
    Given an array A consisting of N integers, returns 1 if there exists a triangular triplet
    for this array and returns 0 otherwise.

    :param A: A non-empty array of integers.
    :return: 1 if there exists a triangular triplet, 0 otherwise.
    """
    # If the length of the array is less than 3, it's impossible to form a triplet
    if len(A) < 3:
        return 0

    # Sort the array in ascending order
    A.sort()

    # Iterate over the array to check for triangular triplets
    for i in range(len(A) - 2):
        # Check the triangular condition
        if A[i] + A[i+1] > A[i+2]:
            return 1

    # No triangular triplet found
    return 0

# Example usage:
input_array1 = [10, 2, 5, 1, 8, 20]
result1 = solution(input_array1)
print(result1)  # Output: 1

input_array2 = [10, 50, 5, 1]
result2 = solution(input_array2)
print(result2)  # Output: 0
