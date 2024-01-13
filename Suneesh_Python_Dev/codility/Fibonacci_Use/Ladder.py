def solution(A, B):
    # Find the maximum rung in A and ensure it's at least 2
    max_rung = max(max(A), 2)

    # Calculate the modulo value based on the maximum value in B
    mod_value = 2 ** max(B)

    # Calculate Fibonacci numbers up to max_rung modulo mod_value
    fib_numbers = [0] * (max_rung + 1)
    fib_numbers[1] = 1

    # Calculate Fibonacci numbers using dynamic programming
    for i in range(2, max_rung + 1):
        fib_numbers[i] = (fib_numbers[i - 1] + fib_numbers[i - 2]) % mod_value

    # Calculate the result based on A and B
    result = []
    for i in range(len(A)):
        # Use the precomputed Fibonacci numbers and apply modulo
        result.append(fib_numbers[A[i]] % (2 ** B[i]))

    return result


# Example usage:
A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
result = solution(A, B)
print("Result:", result)
