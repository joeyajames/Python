import random
from dataclasses import dataclass


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value: int):
        if value is not None:
            if self.data is None:
                self.data = value
            elif self.data > value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif self.data < value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def preorder_traversal(self, node):
        result = []
        if node:
            result.append(node.data)
            result = result + self.preorder_traversal(node.left)
            result = result + self.preorder_traversal(node.right)
        return result

    def in_order_traversal(self, node):
        result = []
        if node:
            result = self.in_order_traversal(node.left)
            result.append(node.data)
            result = result + self.in_order_traversal(node.right)
        return result

    def post_order_traversal(self, node):
        result = []
        if node:
            result = self.post_order_traversal(node.left)
            result = result + self.post_order_traversal(node.right)
            result.append(node.data)
        return result

def max_depth(root : Node) -> int:
        if root is None:
            return 0
        else:
            lDepth = max_depth(root.left)
            rDepth = max_depth(root.right)

            if(lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1


def create_tree() -> Node:
    tree = Node()
    list_to_insert = [random.randint(i, 100) for i in range(0, 5)]
    print(f"List to Insert = {list_to_insert}")
    [tree.insert(element) for element in list_to_insert]
    return tree


binary_tree = create_tree()

print(binary_tree.preorder_traversal(binary_tree))
print(binary_tree.in_order_traversal(binary_tree))
print(binary_tree.post_order_traversal(binary_tree))

print(max_depth(binary_tree))
print(max_depth(Node()))

