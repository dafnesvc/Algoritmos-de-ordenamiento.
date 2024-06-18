"""Dafne Villanueva 21310176
Ordenamiento de árbol.---->El método de ordenamiento de árbol, también conocido como Heap Sort en su implementación más común, es un algoritmo
eficiente que utiliza una estructura de datos llamada heap (montículo) para organizar elementos. """

def heapify(arr, n, i):
    # Inicializamos el índice del nodo raíz y los índices de los hijos izquierdo y derecho
    largest = i  # nodo raíz
    left = 2 * i + 1  # hijo izquierdo
    right = 2 * i + 2  # hijo derecho
    
    # Comparamos el nodo raíz con el hijo izquierdo para ver si es mayor
    if left < n and arr[i] < arr[left]:
        largest = left
    
    # Comparamos el nodo raíz (o el mayor hijo izquierdo) con el hijo derecho para ver si es mayor
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    # Si el nodo raíz no es el mayor, lo intercambiamos con el mayor de los hijos
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Llamamos recursivamente a heapify para asegurarnos de que el subárbol afectado también sea un heap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Construimos un max heap (montículo máximo) empezando desde el último nodo no hoja
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraemos elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        # Intercambiamos el primer elemento (el más grande en un max heap) con el último elemento del heap
        arr[i], arr[0] = arr[0], arr[i]
        # Llamamos a heapify en el heap reducido
        heapify(arr, i, 0)
    
    # Devolvemos la lista ordenada
    return arr

# Ejemplo de uso
lista = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista)

# Llamamos a la función de ordenación por heap sort y almacenamos el resultado en 'ordenada'
ordenada = heap_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", ordenada)
