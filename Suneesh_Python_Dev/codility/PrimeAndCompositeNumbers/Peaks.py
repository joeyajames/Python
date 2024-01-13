def solution(A):
    """
    Given a non-empty array A of N integers, returns the maximum number of blocks into which A can be divided.

    A peak is an array element larger than its neighbors. The goal is to divide the array into blocks containing the same number of elements,
    ensuring that every block has at least one peak.

    For example, given array A:
    A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    The function should return 3, as A can be divided into three blocks, each containing a peak.

    Assumptions:
    - N is an integer within the range [1..100,000]
    - Each element of array A is an integer within the range [0..1,000,000,000].
    """

    N = len(A)
    peaks = []  # Indices of peaks in the array

    # Find peaks in the array
    for i in range(1, N - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    # Check for each possible number of blocks
    for blocks in range(len(peaks), 0, -1):
        if N % blocks == 0:  # Must be divisible into equal blocks
            block_size = N // blocks
            found_peaks = 0

            # Check if each block contains at least one peak
            for peak in peaks:
                if peak // block_size == found_peaks:
                    found_peaks += 1

                # Break if all peaks are found
                if found_peaks == blocks:
                    return blocks

    return 0  # If no valid division is found

# Example usage:
A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
result = solution(A)
print("Maximum Number of Blocks:", result)
