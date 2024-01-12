def solution(A, B):
    result = ""

    while A > 0 or B > 0:
        if A > B:
            if len(result) >= 2 and result[-2:] == 'aa':
                result += 'b'
                B -= 1
            else:
                result += 'a'
                A -= 1
        else:
            if len(result) >= 2 and result[-2:] == 'bb':
                result += 'a'
                A -= 1
            else:
                result += 'b'
                B -= 1

    return result

# Example usage:
A = 5
B = 3
result = solution(A, B)
print(result)  # Output: "aabaabab" or any other valid string

A = 3
B = 3
result = solution(A, B)
print(result)  # Output: "ababab" or any other valid string

A = 1
B = 4
result = solution(A, B)
print(result)  # Output: "bbabb" or any other valid string
