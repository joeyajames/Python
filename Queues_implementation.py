# Queue Implementation in Python
# This file includes two queue implementations:
# 1. LinkedListQueue: using a custom Node class.
# 2. ArrayQueue: using Python's built-in list.

class Node:
    """A class representing a node in a linked list queue."""
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class LinkedListQueue:
    """A Queue implementation using a doubly linked list."""
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, x):
        """Add an element to the back of the queue."""
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.head.item
        self.head = self.head.next
        if self.head is not None:
            self.head.previous = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.length == 0

    def size(self):
        """Return the number of elements in the queue."""
        return self.length

    def display(self):
        """Return a list representation of the queue from front to back."""
        arr = []
        current = self.head
        while current:
            arr.append(current.item)
            current = current.next
        return arr


class ArrayQueue:
    """A Queue implementation using a dynamic array (Python list)."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0

    def enqueue(self, data):
        """Add an element to the back of the queue."""
        self.items.append(data)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)

    def display(self):
        """Return a list representation of the queue from front to back."""
        return list(self.items)


def main():
    print("--- Testing ArrayQueue ---")
    que = ArrayQueue()
    que.enqueue('google')
    que.enqueue('youtube')
    que.enqueue('udemy')
    que.enqueue('udacity')
    print("Initial queue:", que.display())
    print("Dequeued:", que.dequeue())
    print("Dequeued:", que.dequeue())
    print("Remaining queue:", que.display())

    print("\n--- Testing LinkedListQueue ---")
    ll_que = LinkedListQueue()
    ll_que.enqueue('google')
    ll_que.enqueue('youtube')
    ll_que.enqueue('udemy')
    ll_que.enqueue('udacity')
    print("Initial queue:", ll_que.display())
    print("Dequeued:", ll_que.dequeue())
    print("Dequeued:", ll_que.dequeue())
    print("Remaining queue:", ll_que.display())


if __name__ == "__main__":
    main()
