def solution(A):
    """
    Given a non-empty array A, returns the value of the maximal product of any triplet.

    :param A: A non-empty array of integers.
    :return: The maximal product of any triplet.
    """
    # Sort the array in ascending order
    A.sort()

    # Calculate the product of the two smallest numbers and the largest number
    max_product1 = A[0] * A[1] * A[-1]

    # Calculate the product of the three largest numbers
    max_product2 = A[-1] * A[-2] * A[-3]

    # Return the maximum of the two calculated products
    return max(max_product1, max_product2)

# Example usage:
input_array = [-3, 1, 2, -2, 5, 6]
result = solution(input_array)
print(result)  # Output: 60
