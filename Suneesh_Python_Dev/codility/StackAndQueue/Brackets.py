def solution(S):
    """
    Given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

    :param S: Input string to check for proper nesting.
    :return: 1 if S is properly nested, 0 otherwise.
    """
    # Create a stack to track opening brackets
    stack = []

    # Define a dictionary to map closing brackets to their corresponding opening brackets
    brackets_mapping = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the string
    for char in S:
        # If the character is a closing bracket
        if char in brackets_mapping:
            # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'

            # Check if the popped element matches the corresponding opening bracket
            if brackets_mapping[char] != top_element:
                return 0  # Improperly nested, return 0
        else:
            stack.append(char)  # Push opening brackets onto the stack

    # If the stack is empty, all brackets were properly nested
    return 1 if not stack else 0

# Example usage:
input_string1 = "{[()()]}"
input_string2 = "([)()]"
result1 = solution(input_string1)
result2 = solution(input_string2)
print(result1)  # Output: 1
print(result2)  # Output: 0
