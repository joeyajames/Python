def solution(S, P, Q):
    N = len(S)
    M = len(P)

    # Create arrays for prefix sums of each nucleotide type
    prefix_sums = [[0] * (N + 1) for _ in range(4)]

    for i in range(1, N + 1):
        for j in range(4):
            prefix_sums[j][i] = prefix_sums[j][i - 1]

        if S[i - 1] == 'A':
            prefix_sums[0][i] += 1
        elif S[i - 1] == 'C':
            prefix_sums[1][i] += 1
        elif S[i - 1] == 'G':
            prefix_sums[2][i] += 1
        elif S[i - 1] == 'T':
            prefix_sums[3][i] += 1

    # Process each query
    result = []
    for k in range(M):
        start_position = P[k]
        end_position = Q[k] + 1  # Include the end position in the range

        for nucleotide in range(4):
            if prefix_sums[nucleotide][end_position] - prefix_sums[nucleotide][start_position] > 0:
                result.append(nucleotide + 1)  # Nucleotide impact factor is 1-indexed
                break

    return result


# Example usage:
S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
result = solution(S, P, Q)
print(result)
