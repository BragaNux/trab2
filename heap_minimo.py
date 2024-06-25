class MinHeap:
    def __init__(self):
        self.heap = []  # Inicializa uma lista vazia que servirá como o heap.

    def insert(self, key):
        self.heap.append(key)  # Adiciona o novo valor no final do heap.
        self.heapifyUp(len(self.heap) - 1)  # Ajusta o heap para cima a partir do último índice.

    def heapifyUp(self, index):
        parent = (index - 1) // 2  # Calcula o índice do nó pai.
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Troca o nó com o pai se o nó for menor.
            self.heapifyUp(parent)  # Recursivamente ajusta o heap para cima a partir do nó pai.

    def extract_min(self):
        if len(self.heap) == 0:
            return None  # Se o heap estiver vazio, retorna None.
        if len(self.heap) == 1:
            return self.heap.pop()  # Se tiver apenas um elemento, retorna e remove esse elemento.

        root = self.heap[0]  # Guarda o valor da raiz, que é o mínimo.
        self.heap[0] = self.heap.pop()  # Move o último elemento para a raiz.
        self.heapifyDown(0)  # Ajusta o heap para baixo a partir da raiz.
        return root  # Retorna o valor mínimo que foi removido.

    def heapifyDown(self, index):
        smallest = index  # Começa assumindo que o índice atual é o menor.
        left_child = 2 * index + 1  # Calcula o índice do filho esquerdo.
        right_child = 2 * index + 2  # Calcula o índice do filho direito.

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child  # Atualiza o menor se o filho esquerdo for menor que o atual.

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child  # Atualiza o menor se o filho direito for menor que o atual.

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # Troca o índice atual pelo menor encontrado.
            self.heapifyDown(smallest)  # Recursivamente ajusta o heap para baixo a partir do menor.

    def delete(self, key):
        try:
            index = self.heap.index(key)  # Localiza o índice do elemento a ser removido.
            self.heap[index] = self.heap.pop()  # Substitui o elemento pelo último e remove o último.
            parent_index = (index - 1) // 2  # Calcula o índice do nó pai.
            if index > 0 and self.heap[index] < self.heap[parent_index]:
                self.heapifyUp(index)  # Se o elemento é menor que o pai, ajusta para cima.
            else:
                self.heapifyDown(index)  # Caso contrário, ajusta para baixo.
        except ValueError:
            print("Key not found in the heap")  # Trata o erro caso o elemento não esteja no heap.

# Exemplo de uso
min_heap = MinHeap()  # Cria uma instância do MinHeap.
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(30)
min_heap.insert(60)
min_heap.insert(70)
min_heap.insert(80)
min_heap.insert(12)

print("Heap após inserções:")
print(min_heap.heap)  # Exibe o heap após as inserções.

min_heap.delete(20)
print("Heap após remover 20:")
print(min_heap.heap)  # Exibe o heap após remover o elemento 20.

print("Elemento mínimo extraído:")
print(min_heap.extract_min())  # Exibe o valor mínimo extraído, que é o elemento na raiz.

print("Heap após extrair o mínimo:")
print(min_heap.heap)  # Exibe o heap após extrair o mínimo.
