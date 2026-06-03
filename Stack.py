# Stack Implementation in Python
# This file includes two stack implementations:
# 1. ArrayStack: using Python's built-in list.
# 2. LinkedListStack: using a custom Node class.

class Node:
    """A class representing a node in a linked list stack."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedListStack:
    """A Stack implementation using a singly linked list."""
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, data):
        """Push an element onto the stack."""
        new_node = Node(data, self.head)
        self.head = new_node
        self._size += 1

    def pop(self):
        """Pop and return the top element of the stack. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.head
        self.head = self.head.next_node
        self._size -= 1
        return popped_node.data

    def peek(self):
        """Return the top element without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek on empty stack")
        return self.head.data

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return self.head is None

    def size(self):
        """Return the number of elements in the stack."""
        return self._size

    def __str__(self):
        """Return a string representation of the stack."""
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.data))
            current = current.next_node
        return "Top -> " + " -> ".join(elements) if elements else "Empty Stack"


class ArrayStack:
    """A Stack implementation using a dynamic array (Python list)."""
    def __init__(self):
        self.items = []

    def push(self, data):
        """Push an element onto the stack."""
        self.items.append(data)

    def pop(self):
        """Pop and return the top element of the stack. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek on empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return "Bottom -> " + str(self.items) + " <- Top"


def main():
    print("--- Testing ArrayStack ---")
    array_stack = ArrayStack()
    print(f"Is empty? {array_stack.is_empty()}")
    
    array_stack.push("Google")
    array_stack.push("YouTube")
    array_stack.push("Udemy")
    
    print(array_stack)
    print(f"Stack size: {array_stack.size()}")
    print(f"Peek top: {array_stack.peek()}")
    print(f"Popped: {array_stack.pop()}")
    print(array_stack)
    
    print("\n--- Testing LinkedListStack ---")
    ll_stack = LinkedListStack()
    print(f"Is empty? {ll_stack.is_empty()}")
    
    ll_stack.push(10)
    ll_stack.push(20)
    ll_stack.push(30)
    
    print(ll_stack)
    print(f"Stack size: {ll_stack.size()}")
    print(f"Peek top: {ll_stack.peek()}")
    print(f"Popped: {ll_stack.pop()}")
    print(ll_stack)


if __name__ == "__main__":
    main()
