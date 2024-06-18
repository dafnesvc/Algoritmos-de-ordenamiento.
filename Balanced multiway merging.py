"""Dafne Villanueva 21310176
Balanced multiway merging--->Este código implementa Balanced Multiway Merging de manera simplificada. Divide la lista original en sub-listas de tamaño k,
las ordena individualmente y luego las fusiona utilizando un heap para obtener la lista final ordenada [1, 3, 5, 6, 7, 8, 11, 12, 13]."""


import heapq

# Función para dividir la lista en sub-listas de tamaño k
def split_into_chunks(arr, k):
    chunks = []
    for i in range(0, len(arr), k):
        chunks.append(arr[i:i + k])
    return chunks

# Función para fusionar múltiples listas ordenadas
def multiway_merge(lists):
    result = []
    heap = []
    
    # Inicializar el heap con el primer elemento de cada lista
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.pop(0), i))
    
    while heap:
        val, idx = heapq.heappop(heap)
        result.append(val)
        
        # Si hay elementos restantes en la lista correspondiente al índice, añadir el siguiente elemento al heap
        if lists[idx]:
            heapq.heappush(heap, (lists[idx].pop(0), idx))
    
    return result

# Función principal para ordenar mediante Balanced Multiway Merging
def balanced_multiway_merge_sort(arr, k):
    n = len(arr)
    
    # Dividir la lista en sub-listas de tamaño k
    chunks = split_into_chunks(arr, k)
    
    # Ordenar cada sub-lista individualmente
    for i in range(len(chunks)):
        chunks[i].sort()
    
    # Realizar el multiway merge sobre las listas ordenadas
    sorted_arr = multiway_merge(chunks)
    
    return sorted_arr

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7, 1, 3, 8]
k = 3  # Tamaño de las sub-listas

print("Lista original:", arr)

# Aplicar el método Balanced Multiway Merging para ordenar la lista
sorted_arr = balanced_multiway_merge_sort(arr, k)

print("Lista ordenada:", sorted_arr)
