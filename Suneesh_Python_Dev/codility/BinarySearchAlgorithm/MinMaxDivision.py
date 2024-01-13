def solution(K, M, A):
    """
    Given integers K, M, and a non-empty array A consisting of N integers,
    returns the minimal large sum by dividing the array into K blocks of consecutive elements.

    Assumptions:
    - N and K are integers within the range [1..100,000];
    - M is an integer within the range [0..10,000];
    - Each element of array A is an integer within the range [0..M].
    """

    def is_valid_large_sum(mid):
        """
        Checks if it is possible to divide the array into K blocks
        with a maximum block sum less than or equal to mid.
        """
        blocks = 0
        current_sum = 0

        for element in A:
            current_sum += element

            # If the current_sum exceeds mid, start a new block
            if current_sum > mid:
                current_sum = element
                blocks += 1

                # If the number of blocks exceeds K, return False
                if blocks >= K:
                    return False

        return True

    # Binary search to find the minimal large sum
    lower_bound = max(A)
    upper_bound = sum(A)
    result = 0

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if is_valid_large_sum(mid):
            # If it is possible to divide the array into K blocks with max sum <= mid
            # Update the result and search in the lower half
            result = mid
            upper_bound = mid - 1
        else:
            # If not possible, search in the upper half
            lower_bound = mid + 1

    return result

# Example usage:
K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]
result = solution(K, M, A)
print("Minimal large sum:", result)
