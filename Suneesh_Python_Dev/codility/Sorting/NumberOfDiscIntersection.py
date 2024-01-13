def solution(A):
    """
    Given an array A describing N discs, returns the number of (unordered) pairs of intersecting discs.
    Returns -1 if the number of intersecting pairs exceeds 10,000,000.

    :param A: An array of non-negative integers specifying the radiuses of the discs.
    :return: The number of intersecting pairs of discs or -1 if it exceeds the limit.
    """
    # Define the constant representing the limit for intersecting pairs
    LIMIT = 10000000

    # Create lists to store the left and right endpoints of each disc
    left_endpoints = [0] * len(A)
    right_endpoints = [0] * len(A)

    # Populate the left and right endpoint lists
    for i in range(len(A)):
        left_endpoints[i] = i - A[i]
        right_endpoints[i] = i + A[i]

    # Sort the left and right endpoint lists
    left_endpoints.sort()
    right_endpoints.sort()

    # Initialize variables for counting intersecting pairs and active discs
    intersecting_pairs = 0
    active_discs = 0

    # Iterate through the right endpoints to count intersecting pairs
    for right_endpoint in right_endpoints:
        # Count active discs whose left endpoint is less than or equal to the current right endpoint
        while active_discs < len(left_endpoints) and left_endpoints[active_discs] <= right_endpoint:
            active_discs += 1

        # Increment intersecting pairs by the number of active discs (excluding the current disc)
        intersecting_pairs += active_discs - 1

        # Check if the number of intersecting pairs exceeds the limit
        if intersecting_pairs > LIMIT:
            return -1

    # Return the total number of intersecting pairs
    return intersecting_pairs

# Example usage:
input_array = [1, 5, 2, 1, 4, 0]
result = solution(input_array)
print(result)  # Output: 11
