def solution(A):
    """
    Given a non-empty array A of N integers, returns the maximal result that can be achieved on the board represented by array A.

    A game for one player is played on a board consisting of N consecutive squares, numbered from 0 to N − 1. There is a number written on each square. A non-empty array A of N integers contains the numbers written on the squares. Moreover, some squares can be marked during the game.

    At the beginning of the game, there is a pebble on square number 0, and this is the only square on the board that is marked. The goal of the game is to move the pebble to square number N − 1.

    During each turn, a six-sided die is thrown, and the number K, which shows on the upper face after the die comes to rest, is considered. Then the pebble is moved from square number I to square number I + K, provided that square number I + K exists. If square number I + K does not exist, the die is thrown again until a valid move is obtained. Finally, square number I + K is marked.

    After the game finishes (when the pebble is standing on square number N − 1), the result is calculated. The result of the game is the sum of the numbers written on all marked squares.

    For example, given the following array:
    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2
    one possible game could be as follows:
    the pebble is on square number 0, which is marked;
    we throw 3; the pebble moves from square number 0 to square number 3; we mark square number 3;
    we throw 5; the pebble does not move, since there is no square number 8 on the board;
    we throw 2; the pebble moves to square number 5; we mark this square, and the game ends.
    The marked squares are 0, 3, and 5, so the result of the game is 1 + 9 + (−2) = 8. This is the maximal possible result that can be achieved on this board.

    Assumptions:
    - N is an integer within the range [2..100,000];
    - Each element of array A is an integer within the range [−10,000..10,000].
    """

    N = len(A)
    max_result = float('-inf')  # Initialize the max result to negative infinity
    current_position = 0  # Initialize the current position to 0
    marked_squares = {0}  # Use a set to keep track of marked squares

    while current_position != N - 1:
        # Throw the die
        die_result = A[current_position]

        # Move the pebble to the new position
        new_position = current_position + die_result

        # Check if the new position is valid
        if 0 <= new_position < N and new_position not in marked_squares:
            marked_squares.add(new_position)  # Mark the new square
            current_position = new_position  # Update the current position
            max_result = max(max_result, sum(A[i] for i in marked_squares))  # Update the max result
        else:
            break  # Break the loop if the new position is not valid

    return max_result

# Example usage:
A = [1, -2, 0, 9, -1, -2]
result = solution(A)
print("Maximal result:", result)
