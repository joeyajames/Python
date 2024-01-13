def solution(A):
    """
    Given a non-empty array A consisting of N integers, returns the minimal abs sum of two
    for any pair of indices in this array.

    The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|,
    for 0 ≤ P ≤ Q < N.

    Assumptions:
    - N is an integer within the range [1..100,000];
    - Each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
    """

    # Sort the array in non-decreasing order
    A.sort()

    # Initialize pointers for the two ends of the array
    left, right = 0, len(A) - 1

    # Initialize the minimal abs sum of two
    min_abs_sum = float('inf')

    # Move the pointers towards each other until they meet
    while left <= right:
        # Calculate the abs sum for the current pair of indices
        current_sum = A[left] + A[right]

        # Update the minimal abs sum
        min_abs_sum = min(min_abs_sum, abs(current_sum))

        # Move the pointers based on the current sum
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            # If the sum is 0, it cannot get smaller, return early
            return 0

    return min_abs_sum

# Example usage:
A1 = [1, 4, -3]
result1 = solution(A1)
print("Minimal abs sum of two for A1:", result1)

A2 = [-8, 4, 5, -10, 3]
result2 = solution(A2)
print("Minimal abs sum of two for A2:", result2)
