def solution(X, Y, D):
    distance_to_cover = Y - X
    jumps_needed = distance_to_cover // D

    # If there is a remainder, one additional jump is needed
    if distance_to_cover % D != 0:
        jumps_needed += 1

    return jumps_needed

# Example usage:
X1, Y1, D1 = 10, 85, 30
print(solution(X1, Y1, D1))  # Output: 3
