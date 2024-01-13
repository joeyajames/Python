def solution(A, B):
    """
    Given two non-empty arrays A and B consisting of N integers,
    returns the number of fish that will stay alive.

    :param A: Array containing sizes of the fish.
    :param B: Array containing directions of the fish (0 for upstream, 1 for downstream).
    :return: Number of fish that will stay alive.
    """
    # Stack to track downstream fish
    downstream_stack = []

    # Count of fish that will stay alive
    alive_fish_count = 0

    # Iterate through each fish
    for i in range(len(A)):
        size_i = A[i]
        direction_i = B[i]

        # If fish is moving upstream
        if direction_i == 0:
            # Check if downstream fish will be eaten by the current upstream fish
            while downstream_stack:
                downstream_size = downstream_stack.pop()

                # Current downstream fish is eaten by the upstream fish
                if downstream_size < size_i:
                    continue
                else:
                    # Current downstream fish survives and is added back to the stack
                    downstream_stack.append(downstream_size)
                    break
            else:
                # If no downstream fish survives, the current upstream fish stays alive
                alive_fish_count += 1
        else:
            # Fish is moving downstream, add it to the stack
            downstream_stack.append(size_i)

    # The remaining downstream fish are alive
    alive_fish_count += len(downstream_stack)

    return alive_fish_count

# Example usage:
fish_sizes = [4, 3, 2, 1, 5]
fish_directions = [0, 1, 0, 0, 0]
result = solution(fish_sizes, fish_directions)
print(result)  # Output: 2



# --------------
empty , first_new , last_new = "", "Suneesh", "Joshi"
results = empty or first_new or last_new
print(results)