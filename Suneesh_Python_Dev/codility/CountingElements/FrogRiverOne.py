def solution(X, A):
    covered_positions = set()

    for time, position in enumerate(A):
        covered_positions.add(position)

        if len(covered_positions) == X:
            return time

    return -1  # If all positions are not covered


# Example usage:
X = 9
A = [1, 3, 1, 4, 2, 3, 5, 8,4]
print(solution(X, A))  # Output: 6
