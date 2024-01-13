def solution(A):
    """
    Given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors for each element.

    For each number A[i], where 0 ≤ i < N, count the number of elements in the array that are not divisors of A[i].

    For example, given array A = [3, 1, 2, 3, 6]:
    - A[0] = 3, non-divisors: 2, 6
    - A[1] = 1, non-divisors: 3, 2, 3, 6
    - A[2] = 2, non-divisors: 3, 3, 6
    - A[3] = 3, non-divisors: 2, 6
    - A[4] = 6, no non-divisors

    The function should return [2, 4, 3, 2, 0].

    Assumptions:
    - N is an integer within the range [1..50,000]
    - Each element of array A is an integer within the range [1..2 * N].
    """

    N = len(A)
    max_value = max(A)  # Find the maximum value in the array
    counter = [0] * (2 * N + 1)  # Initialize a counter array for counting occurrences
    result = []

    # Count occurrences of each number in the array
    for num in A:
        counter[num] += 1

    # Iterate through each number in the array
    for num in A:
        divisors = 0

        # Find divisors of the current number
        for div in range(1, int(num**0.5) + 1):
            if num % div == 0:
                divisors += counter[div]  # Add occurrences of divisor
                if num // div != div:
                    divisors += counter[num // div]  # Add occurrences of the other divisor

        # Calculate non-divisors by subtracting total divisors from the total count
        result.append(N - divisors)

    return result

# Example usage:
A = [3, 1, 2, 3, 6]
result = solution(A)
print("Non-Divisors Count:", result)
