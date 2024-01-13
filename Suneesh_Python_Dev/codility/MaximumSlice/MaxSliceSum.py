def solution(A):
    N = len(A)

    # Edge case: if there is only one element in the array, return that element
    if N == 1:
        return A[0]

    # Initialize variables to keep track of maximum sum and current sum
    max_sum = A[0]
    current_sum = A[0]

    # Iterate through the array starting from the second element
    for num in A[1:]:
        # Calculate the current sum by either continuing the current slice or starting a new slice
        current_sum = max(num, current_sum + num)

        # Update the maximum sum if a higher sum is encountered
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
array_A = [3, 2, -6, 4, 0]
result = solution(array_A)
print("Maximum Sum of any Slice:", result)
