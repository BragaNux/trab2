import math  # Importa o módulo math para funções matemáticas.

# Criando uma árvore de Fibonacci
class FibonacciTree:
    def __init__(self, value):
        self.value = value  # Valor do nó.
        self.child = []  # Lista de árvores filhas.
        self.order = 0  # Ordem da árvore, representando o número de filhos.

    # Adicionando uma árvore ao final da lista de filhos.
    def add_at_end(self, t):
        self.child.append(t)  # Adiciona a árvore t como um filho.
        self.order = self.order + 1  # Incrementa a ordem da árvore.

# Criando um heap de Fibonacci
class FibonacciHeap:
    def __init__(self):
        self.trees = []  # Lista de árvores no heap.
        self.least = None  # Aponta para a árvore com o menor valor.
        self.count = 0  # Contagem de nós no heap.

    # Inserir um nó no heap
    def insert_node(self, value):
        new_tree = FibonacciTree(value)  # Cria uma nova árvore com o valor.
        self.trees.append(new_tree)  # Adiciona a nova árvore à lista de árvores.
        if (self.least is None or value < self.least.value):
            self.least = new_tree  # Atualiza o ponteiro para o menor valor.
        self.count = self.count + 1  # Incrementa a contagem de nós.

    # Obter o valor mínimo
    def get_min(self):
        if self.least is None:
            return None  # Retorna None se não houver elementos.
        return self.least.value  # Retorna o valor do menor elemento.

    # Extrair o valor mínimo
    def extract_min(self):
        smallest = self.least  # Armazena o menor valor.
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)  # Adiciona os filhos da menor árvore à lista de árvores.
            self.trees.remove(smallest)  # Remove a árvore com o menor valor.
            if self.trees == []:
                self.least = None  # Se o heap está vazio, define least como None.
            else:
                self.least = self.trees[0]  # Define a nova árvore com o menor valor.
                self.consolidate()  # Consolida o heap para manter as propriedades do heap de Fibonacci.
            self.count = self.count - 1  # Decrementa a contagem de nós.
            return smallest.value  # Retorna o valor do menor elemento.

    # Consolidar o heap
    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]  # Cria uma lista auxiliar para consolidação.

        while self.trees != []:
            x = self.trees[0]  # Pega a primeira árvore.
            order = x.order  # Ordem da árvore x.
            self.trees.remove(x)  # Remove x da lista de árvores.
            while aux[order] is not None:
                y = aux[order]  # Árvore na mesma ordem de x.
                if x.value > y.value:
                    x, y = y, x  # Garante que x seja a árvore com menor valor.
                x.add_at_end(y)  # Adiciona y como um filho de x.
                aux[order] = None  # Limpa a posição em aux.
                order = order + 1  # Incrementa a ordem para a próxima iteração.
            aux[order] = x  # Adiciona x atualizado em aux.

        self.least = None  # Redefine o ponteiro para o menor valor.
        for k in aux:
            if k is not None:
                self.trees.append(k)  # Adiciona árvores de aux de volta ao heap.
                if (self.least is None or k.value < self.least.value):
                    self.least = k  # Atualiza o ponteiro para o menor valor.

def floor_log(x):
    return math.frexp(x)[1] - 1  # Retorna o logaritmo base 2 de x, ajustado para baixo.

fibonacci_heap = FibonacciHeap()  # Cria um novo heap de Fibonacci.

# Inserindo nós no heap de Fibonacci.
fibonacci_heap.insert_node(7)
fibonacci_heap.insert_node(3)
fibonacci_heap.insert_node(17)
fibonacci_heap.insert_node(24)

# Exibindo o valor mínimo do heap de Fibonacci.
print('the minimum value of the fibonacci heap: {}'.format(fibonacci_heap.get_min()))

# Removendo e exibindo o valor mínimo do heap de Fibonacci.
print('the minimum value removed: {}'.format(fibonacci_heap.extract_min()))
