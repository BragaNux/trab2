class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.heapifyUp(len(self.heap) - 1)

    def heapifyUp(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapifyUp(parent)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyDown(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapifyDown(smallest)

    def delete(self, key):
        try:
            index = self.heap.index(key)
            self.heap[index] = self.heap.pop()
            parent_index = (index - 1) // 2
            if index > 0 and self.heap[index] < self.heap[parent_index]:
                self.heapifyUp(index)
            else:
                self.heapifyDown(index)
        except ValueError:
            print("Key not found in the heap")

# Exemplo de uso
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(30)
min_heap.insert(60)
min_heap.insert(70)
min_heap.insert(80)
min_heap.insert(12)

print("Heap após inserções:")
print(min_heap.heap)  # Saída esperada: [5, 10, 20, 30]

min_heap.delete(20)
print("Heap após remover 20:")
print(min_heap.heap)  # Saída esperada: [5, 10, 30]

print("Elemento mínimo extraído:")
print(min_heap.extract_min())  # Saída esperada: 5

print("Heap após extrair o mínimo:")
print(min_heap.heap)  # Saída esperada: [10, 30]
