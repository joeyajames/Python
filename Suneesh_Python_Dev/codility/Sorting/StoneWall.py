def solution(H):
    # Stack to keep track of heights and corresponding block counts
    stack = []

    # Variable to store the total number of blocks
    block_count = 0

    # Iterate through each height in the array
    for height in H:
        # Pop heights from the stack until a height greater than the current height is found
        while stack and stack[-1] > height:
            stack.pop()

        # If the stack is empty or the current height is greater than the top of the stack
        if not stack or stack[-1] < height:
            # Add the current height to the stack and increment block_count
            stack.append(height)
            block_count += 1

    return block_count


# Example usage:
result = solution([8, 8, 5, 7, 9, 8, 7, 4, 8])  # Expected output: 7
print("Result:", result)
