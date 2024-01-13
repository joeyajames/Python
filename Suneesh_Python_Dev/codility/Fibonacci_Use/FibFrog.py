def solution(A):
    # Function to calculate Fibonacci numbers up to a given limit
    def calculate_fibonacci(limit):
        fib = [0, 1]

        while fib[-1] <= limit:
            fib.append(fib[-1] + fib[-2])

        return fib[:-1]  # Exclude the last Fibonacci number exceeding the limit

    # Get the Fibonacci numbers up to N
    fibonacci_numbers = calculate_fibonacci(len(A) + 1)

    # Create a set of positions with leaves for faster lookup
    positions_with_leaves = set(i for i, leaf in enumerate(A) if leaf == 1)

    # Initialize variables for dynamic programming
    dp = [-1] * (len(A) + 2)
    dp[0] = 0

    # Iterate through positions
    for position in range(len(A) + 1):
        if dp[position] != -1:  # Check if the position is reachable
            for jump in fibonacci_numbers:
                next_position = position + jump

                # Check if the next position is within the river and has a leaf
                if next_position <= len(A) and next_position not in positions_with_leaves:
                    # Update the minimum number of jumps needed to reach the next position
                    if dp[next_position] == -1 or dp[next_position] > dp[position] + 1:
                        dp[next_position] = dp[position] + 1

    # Return the result
    return dp[-1]


# Example usage:
A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
result = solution(A)
print("Result:", result)
