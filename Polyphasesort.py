"""Dafne Villanueva 21310176
Polyphase sort--->Este código implementa Polyphase Sort de manera simplificada. Divide la lista original en subsecuencias de tamaño k, las ordena individualmente
y luego realiza la fusión utilizando buffers intermedios para obtener la lista final ordenada [1, 3, 5, 6, 7, 8, 11, 12, 13]."""

import heapq

# Función para dividir la lista en subsecuencias de tamaño k
def split_into_sequences(arr, k):
    sequences = []
    for i in range(0, len(arr), k):
        sequences.append(arr[i:i + k])
    return sequences

# Función para realizar una fusión de fases utilizando un buffer
def polyphase_merge(f, buffer_size):
    # Inicializar buffers
    buffers = [[] for _ in range(buffer_size)]
    merged_result = []
    
    # Cargar los primeros elementos de cada secuencia en los buffers
    for i in range(buffer_size):
        buffers[i].extend(next(f, []))
    
    # Usar un heap para obtener el menor elemento disponible
    heap = [(buffers[i][0], i) for i in range(buffer_size) if buffers[i]]
    heapq.heapify(heap)
    
    while heap:
        val, buffer_idx = heapq.heappop(heap)
        merged_result.append(val)
        
        # Obtener el siguiente elemento del buffer correspondiente si hay más elementos
        if buffers[buffer_idx]:
            buffers[buffer_idx].pop(0)
            if buffers[buffer_idx]:
                heapq.heappush(heap, (buffers[buffer_idx][0], buffer_idx))
        
        # Cargar más elementos en el buffer si es necesario
        buffers[buffer_idx].extend(next(f, []))
        if buffers[buffer_idx]:
            heapq.heappush(heap, (buffers[buffer_idx][0], buffer_idx))
    
    return merged_result

# Función principal para ordenar mediante Polyphase Sort
def polyphase_sort(arr, k):
    n = len(arr)
    
    # Dividir la lista en subsecuencias de tamaño k
    sequences = split_into_sequences(arr, k)
    
    # Ordenar cada secuencia individualmente
    for i in range(len(sequences)):
        sequences[i].sort()
    
    # Generar generador para acceder a las secuencias
    def sequence_generator():
        for seq in sequences:
            yield seq
    
    # Realizar la fusión de fases utilizando los buffers
    sorted_arr = polyphase_merge(sequence_generator(), len(sequences))
    
    return sorted_arr

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7, 1, 3, 8]
k = 3  # Tamaño de las subsecuencias

print("Lista original:", arr)

# Aplicar el método Polyphase Sort para ordenar la lista
sorted_arr = polyphase_sort(arr, k)

print("Lista ordenada:", sorted_arr)
