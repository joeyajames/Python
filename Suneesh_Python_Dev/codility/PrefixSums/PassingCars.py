def solution(A):
    east_count = 0  # Count of cars traveling east
    passing_pairs = 0  # Count of passing pairs

    for car_direction in A:
        if car_direction == 0:  # Car traveling east
            east_count += 1
        else:  # Car traveling west
            passing_pairs += east_count

            # Check if the passing pairs exceed the limit
            if passing_pairs > 1000000000:
                return -1

    return passing_pairs

# Example usage:
A = [0, 1, 0, 1, 1]
result = solution(A)
print(result)
