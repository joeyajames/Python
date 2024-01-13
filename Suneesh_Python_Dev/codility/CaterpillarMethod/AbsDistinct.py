def solution(A):
    """
    Given a non-empty array A consisting of N numbers, returns the absolute distinct count of array A.

    The absolute distinct count is the number of distinct absolute values among the elements of the array.

    For example, given array A such that:
    A[0] = -5
    A[1] = -3
    A[2] = -1
    A[3] =  0
    A[4] =  3
    A[5] =  6
    the function should return 5, as there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5, and 6.

    Assumptions:
    - N is an integer within the range [1..100,000];
    - Each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
    - Array A is sorted in non-decreasing order.
    """

    # Initialize the absolute distinct count to 0
    abs_distinct_count = 0

    # Initialize the previous element to a value outside the range of array elements
    prev_element = float('inf')

    # Iterate through the array elements
    for element in A:
        # If the absolute value is not equal to the absolute value of the previous element, increment the count
        if abs(element) != abs(prev_element):
            abs_distinct_count += 1

        # Update the previous element
        prev_element = element

    return abs_distinct_count

# Example usage:
A = [-5, -3, -1, 0, 3, 6]
result = solution(A)
print("Absolute distinct count of array A:", result)
