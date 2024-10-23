class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def minHeapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)

    def extractMin(self):
        if len(self.heap) == 0:
            return float('inf')
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.minHeapify(0)
        return root

# Usage
heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(15)
print("Min element:", heap.extractMin())
