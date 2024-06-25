class MaxHeapNode:
    def __init__(self, doenca, sintomas):
        self.doenca = doenca
        self.sintomas = sintomas

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and len(arr[left].sintomas) > len(arr[largest].sintomas):
        largest = left

    if right < n and len(arr[right].sintomas) > len(arr[largest].sintomas):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def construir_heap(doencas_sintomas):
    heap = [MaxHeapNode(numero_para_doenca[doenca], sintomas) for doenca, sintomas in doencas_sintomas.items()]
    n = len(heap)

    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)
    
    return heap

def inserir_no_heap(heap, doenca, sintomas):
    novo_no = MaxHeapNode(doenca, sintomas)
    heap.append(novo_no)
    i = len(heap) - 1

    while i != 0 and len(heap[(i - 1) // 2].sintomas) < len(heap[i].sintomas):
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2

def remover_no_heap(heap):
    n = len(heap)
    if n == 0:
        return None

    raiz = heap[0]
    heap[0] = heap[n - 1]
    heap.pop()
    heapify(heap, len(heap), 0)

    return raiz

def visualizar_heap(heap):
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
    1: ["febre", "tosse", "dor de cabeça"], # Gripe
    2: ["coriza", "espirros", "dor de garganta"], # Resfriado
    3: ["febre", "tosse seca", "perda de olfato"], # COVID-19
    4: ["febre alta", "dor atrás dos olhos", "manchas vermelhas na pele"], # Dengue
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
