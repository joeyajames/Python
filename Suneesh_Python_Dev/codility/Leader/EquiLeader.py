def solution(A):
    N = len(A)

    # Find the candidate leader using the "leader" algorithm
    candidate_leader, candidate_count = None, 0
    for num in A:
        if candidate_count == 0:
            candidate_leader = num
            candidate_count = 1
        else:
            if candidate_leader == num:
                candidate_count += 1
            else:
                candidate_count -= 1

    # Check if the candidate leader is a real leader (occurs more than half of the array)
    leader_count = A.count(candidate_leader)
    if leader_count <= N // 2:
        return 0  # No equi leader if the candidate is not a real leader

    equi_leader_count, left_leader_count = 0, 0

    # Iterate through the array to find equi leaders
    for idx, num in enumerate(A):
        if num == candidate_leader:
            left_leader_count += 1

        # Check if the left sequence and right sequence have the same leader
        if (
            left_leader_count > (idx + 1) // 2
            and (leader_count - left_leader_count) > (N - idx - 1) // 2
        ):
            equi_leader_count += 1

    return equi_leader_count

# Example usage:
array_A = [4, 3, 4, 4, 4, 2]
result = solution(array_A)
print("Number of Equi Leaders:", result)
