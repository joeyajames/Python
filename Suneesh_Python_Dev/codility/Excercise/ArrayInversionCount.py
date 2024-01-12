def solution(A):
    """
    Computes the number of inversions in array A,
    or returns −1 if it exceeds 1,000,000,000.

    An inversion is a pair of indexes (P, Q) such that P < Q
    and A[Q] < A[P].

    :param A: An array of N integers.
    :return: The number of inversions in A or −1 if it exceeds 1,000,000,000.
    """
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = merge_sort_count(arr[:mid])
        right, right_count = merge_sort_count(arr[mid:])
        merged, merge_count = merge(left, right)

        return merged, left_count + right_count + merge_count

    def merge(left, right):
        merged = []
        i = j = count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    sorted_A, inversions = merge_sort_count(A)

    if inversions > 1_000_000_000:
        return -1
    else:
        return inversions

# Example usage:
arr = [-1, 6, 3, 4, 7, 4]
result = solution(arr)
print(result)  # Output: 4
