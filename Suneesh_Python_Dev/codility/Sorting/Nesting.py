def solution(S):
    stack = []
    if len(S) == 0:
        return 1

    for char in S:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return 0
            else:
                stack.pop()

    return 0 if len(stack) > 0 else 1


print(solution("(())(((((()))))))"))
