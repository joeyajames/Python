from dataclasses import dataclass, field


@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None


def solution(T):
    """
    Given a non-empty binary tree T consisting of N nodes,
    returns its height.

    :param T: A binary tree represented using the Tree class.
    :return: The height of the binary tree.
    """
    if T is None:
        return -1

    left_height = solution(T.l)
    right_height = solution(T.r)

    return 1 + max(left_height, right_height)


# Example usage:
tree = Tree(5, Tree(3, Tree(20), Tree(21)), Tree(10, Tree(1), None))
result = solution(tree)
print(result)  # Output: 2
