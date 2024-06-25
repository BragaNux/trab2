class MaxHeapNode:
    def __init__(self, doenca, sintomas):
        self.doenca = doenca  # Armazena o nome da doença no nó.
        self.sintomas = sintomas  # Armazena uma lista de sintomas associados à doença.

def heapify(arr, n, i):
    largest = i  # Inicialmente, o maior é o nó atual (i).
    left = 2 * i + 1  # Índice do filho esquerdo.
    right = 2 * i + 2  # Índice do filho direito.

    # Verifica se o filho esquerdo existe e se tem mais sintomas do que o atual maior.
    if left < n and len(arr[left].sintomas) > len(arr[largest].sintomas):
        largest = left

    # Verifica se o filho direito existe e se tem mais sintomas do que o atual maior.
    if right < n and len(arr[right].sintomas) > len(arr[largest].sintomas):
        largest = right

    # Se o maior não é o índice atual, troca com o maior e continua a heapify.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def construir_heap(doencas_sintomas):
    # Constrói uma lista de nós do heap a partir dos dados de doenças e sintomas.
    heap = [MaxHeapNode(numero_para_doenca[doenca], sintomas) for doenca, sintomas in doencas_sintomas.items()]
    n = len(heap)

    # Constrói o heap a partir da metade da lista para garantir que todos os nós sejam processados.
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)
    
    return heap

def inserir_no_heap(heap, doenca, sintomas):
    # Cria um novo nó e adiciona ao heap.
    novo_no = MaxHeapNode(doenca, sintomas)
    heap.append(novo_no)
    i = len(heap) - 1

    # Ajusta o heap para cima até o novo nó estar na posição correta.
    while i != 0 and len(heap[(i - 1) // 2].sintomas) < len(heap[i].sintomas):
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2

def remover_no_heap(heap):
    n = len(heap)
    if n == 0:
        return None  # Retorna None se o heap estiver vazio.

    raiz = heap[0]  # A raiz, que é o maior elemento, é armazenada.
    heap[0] = heap[n - 1]  # O último elemento é movido para a raiz.
    heap.pop()  # O último elemento é removido.
    heapify(heap, len(heap), 0)  # Ajusta o heap para baixo a partir da nova raiz.

    return raiz  # Retorna o nó que era a raiz.

def visualizar_heap(heap):
    # Mostra todos os nós no heap.
    for node in heap:
        print(f"Doença: {node.doenca}, Sintomas: {node.sintomas}")

# Dicionário para mapear número da doença de volta para o nome da doença
numero_para_doenca = {
    1: "Gripe",
    2: "Resfriado",
    3: "COVID-19",
    4: "Dengue",
    5: "Pneumonia",
    6: "Sarampo",
    7: "Hepatite",
    8: "Asma"
}

# Dados das doenças e seus sintomas associados com representação numérica
doencas_sintomas = {
    1: ["febre", "tosse", "dor de cabeça"],
    2: ["coriza", "espirros", "dor de garganta"],
    3: ["febre", "tosse seca", "perda de olfato"],
    4: ["febre alta", "dor atrás dos olhos", "manchas vermelhas na pele"],
    5: ["tosse com catarro", "dor no peito", "dificuldade para respirar"], # Pneumonia
    6: ["febre alta", "manchas vermelhas na pele", "tosse persistente"], # Sarampo
    7: ["icterícia", "fadiga", "dor abdominal"], # Hepatite
    8: ["chiado no peito", "falta de ar", "tosse seca"] # Asma
}


heap_maximo = construir_heap(doencas_sintomas)


print("Heap máximo inicial:")
visualizar_heap(heap_maximo)


print("\nInserindo uma nova doença (Influenza) com sintomas ['febre', 'calafrios', 'dores musculares']:")
inserir_no_heap(heap_maximo, "Influenza", ["febre", "calafrios", "dores musculares"])
visualizar_heap(heap_maximo)


print("\nRemovendo a raiz do heap (máximo):")
removido = remover_no_heap(heap_maximo)
print(f"Removido: Doença: {removido.doenca}, Sintomas: {removido.sintomas}")
visualizar_heap(heap_maximo)
