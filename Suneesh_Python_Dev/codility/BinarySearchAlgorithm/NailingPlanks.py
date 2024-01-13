def solution(A, B, C):
    """
    Given two non-empty arrays A and B consisting of N integers
    and a non-empty array C consisting of M integers, returns
    the minimum number of nails that, used sequentially, allow all the planks to be nailed.

    If it is not possible to nail all the planks, returns −1.

    Assumptions:
    - N and M are integers within the range [1..30,000];
    - Each element of arrays A, B, and C is an integer within the range [1..2*M];
    - A[K] ≤ B[K].
    """

    def is_possible(nails, plank_start, plank_end):
        """
        Checks if it's possible to nail a plank with the given nails.
        """
        for i in range(len(nails)):
            if plank_start <= nails[i] <= plank_end:
                return True
        return False

    # Create a list of tuples (plank_start, plank_end)
    planks = list(zip(A, B))

    # Sort the planks based on their end positions
    planks.sort(key=lambda x: x[1])

    # Sort the nails
    nails = sorted(enumerate(C, start=1), key=lambda x: x[1])

    # Binary search to find the minimum number of nails needed
    lower_bound = 1
    upper_bound = len(C)
    result = -1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        # Consider the first 'mid' nails
        current_nails = [nail[1] for nail in nails[:mid]]

        # Check if all planks can be nailed with the current nails
        is_possible_flag = True
        for plank in planks:
            if not is_possible(current_nails, plank[0], plank[1]):
                is_possible_flag = False
                break

        if is_possible_flag:
            # If all planks can be nailed, update the result and search in the lower half
            result = mid
            upper_bound = mid - 1
        else:
            # If not possible, search in the upper half
            lower_bound = mid + 1

    return result

# Example usage:
A = [1, 4, 5, 8]
B = [4, 5, 9, 10]
C = [4, 6, 7, 10, 2]
result = solution(A, B, C)
print("Minimum number of nails:", result)
