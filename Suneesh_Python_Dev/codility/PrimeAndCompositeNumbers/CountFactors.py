def solution(N):
    factors = 0  # Initialize the count of factors

    # Iterate from 1 to the square root of N
    i = 1
    while i * i <= N:
        # If i is a factor, count it
        if N % i == 0:
            factors += 1

            # If i and N/i are different, count N/i as well
            if i != N // i:
                factors += 1

        i += 1

    return factors  # Return the total count of factors

# Example usage:
N = 24
result = solution(N)
print("Number of Factors:", result)
