def solution(N):
    # Initialize the minimum perimeter with a large value
    min_perimeter = float('inf')

    # Iterate from 1 to the square root of N
    i = 1
    while i * i <= N:
        # Check if i is a factor of N
        if N % i == 0:
            # Calculate the corresponding factor and update the perimeter
            factor = N / i
            perimeter = 2 * (i + factor)

            # Update the minimum perimeter if the current one is smaller
            min_perimeter = min(min_perimeter, perimeter)

        i += 1

    return int(min_perimeter)  # Return the minimal perimeter


# Example usage:
N = 30
result = solution(N)
print("Minimal Perimeter:", result)
