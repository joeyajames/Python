class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]  # Initialize heap with a dummy element at index 0
        for i in items:
            self.push(i)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)  # Renamed to follow Python naming conventions

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return None  # Return None instead of False for clarity

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max_value = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max_value = self.heap.pop()
        else:
            max_value = None  # Return None instead of False for clarity
        return max_value

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

# Test the MaxHeap class
m = MaxHeap([95, 3, 21])
m.push(10)
print(m.heap[1:])  # Print heap elements excluding the dummy element
print(m.pop())
