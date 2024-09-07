from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(lst):
    if not lst or lst[0] is None:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    
    while i < len(lst):
        node = queue.popleft()
        
        # Process the left child
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        # Process the right child
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

# Pre-order traversal function
def pre_order_traversal(root):
    cur = root
    stack = []
    res = []
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res

# Build the tree and perform pre-order traversal
lst = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = build_tree_from_list(lst)
print(pre_order_traversal(root))
