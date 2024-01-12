def solution(A, K):
    if not A:
        return A  # Return the array as is if it's empty

    N = len(A)
    K = K % N  # In case K is greater than the length of the array, take the modulo

    if K == 0:
        return A  # If K is 0, no rotation is needed, return the array as is

    rotated_array = A[-K:] + A[:-K]  # Perform the rotation

    return rotated_array

# Example usage:
A1 = [3, 8, 9, 7, 6]
K1 = 3
print(solution(A1, K1))  # Output: [9, 7, 6, 3, 8]

A2 = [0, 0, 0]
K2 = 1
print(solution(A2, K2))  # Output: [0, 0, 0]

A3 = [1, 2, 3, 4]
K3 = 4
print(solution(A3, K3))  # Output: [1, 2, 3, 4]

A4 = []
K4 = 4
print(solution(A4, K4))
