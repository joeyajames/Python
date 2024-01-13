def solution(A):
    N = len(A)

    # Find the candidate dominator using the "leader" algorithm
    candidate_dominator, candidate_count = None, 0
    for num in A:
        if candidate_count == 0:
            candidate_dominator = num
            candidate_count = 1
        else:
            if candidate_dominator == num:
                candidate_count += 1
            else:
                candidate_count -= 1

    # Check if the candidate dominator is a real dominator (occurs more than half of the array)
    dominator_count = A.count(candidate_dominator)
    if dominator_count <= N // 2:
        return -1  # No dominator if the candidate is not a real dominator

    # Find the index of any element with the dominator
    for idx, num in enumerate(A):
        if num == candidate_dominator:
            return idx

    # The code should never reach here, but return -1 for completeness
    return -1

# Example usage:
array_A = [3, 4, 3, 2, 3, -1, 3, 3]
result = solution(array_A)
print("Index of Dominator:", result)
