class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]  # Used a dummy element at index 0
        for i in items:
            self.heap.append(i)
            self._float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self._float_up(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return None
            
    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            max_val = self.heap.pop()
            self._bubble_down(1)
        elif len(self.heap) == 2:
            max_val = self.heap.pop()
        else: 
            max_val = None
        return max_val

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._float_up(parent)

    def _bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubble_down(largest)

m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[1:]))  # Excluding the dummy element when printing heap elements
print(str(m.pop()))  # Output of pop operation
