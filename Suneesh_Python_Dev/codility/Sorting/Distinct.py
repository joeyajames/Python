def solution(A):
    """
    Given an array A consisting of N integers, returns the number of distinct values in array A.

    :param A: An array consisting of N integers.
    :return: The number of distinct values in array A.
    """
    # Use a set to store unique values
    distinct_values = set()

    # Iterate through the array and add each element to the set
    for element in A:
        distinct_values.add(element)

    # Return the count of unique values
    return len(distinct_values)

# Example usage:
input_array = [2, 1, 1, 2, 3, 1]
result = solution(input_array)
print(result)  # Output: 3
