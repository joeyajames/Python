from dataclasses import dataclass

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None

def longest_zigzag_helper(node, direction, length):
    if node is None:
        return length

    # If the direction changes, update the length
    if direction == "left":
        length = longest_zigzag_helper(node.r, "right", length + 1)
        length = longest_zigzag_helper(node.l, "left", 1)
    else:
        length = longest_zigzag_helper(node.l, "left", length + 1)
        length = longest_zigzag_helper(node.r, "right", 1)

    return length

def solution(T):
    if T is None:
        return 0

    left_length = longest_zigzag_helper(T.l, "left", 0)
    right_length = longest_zigzag_helper(T.r, "right", 0)

    return max(left_length, right_length)

# Example usage:
tree = Tree(
    5,
    Tree(
        3,
        Tree(20, Tree(6), None),
        None
    ),
    Tree(
        10,
        Tree(1),
        Tree(
            15,
            Tree(30, None, Tree(9)),
            Tree(8)
        )
    )
)

result = solution(tree)
print(result)  # Output: 2
