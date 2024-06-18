"""Dafne Villanueva 21310176
Distribution of initial runs.---->Este código implementa la fase de distribución de initial runs de manera simplificada. Divide la lista original en runs
iniciales de tamaño k, los ordena individualmente y luego los fusiona para obtener la lista final ordenada [1, 3, 5, 6, 7, 8, 11, 12, 13]."""

import heapq

# Función para dividir la lista en subsecuencias de tamaño k
def split_into_runs(arr, k):
    runs = []
    i = 0
    n = len(arr)
    
    while i < n:
        runs.append(arr[i:i + k])
        i += k
    
    return runs

# Función para ordenar cada run individualmente
def sort_runs(runs):
    for i in range(len(runs)):
        runs[i].sort()
    
    return runs

# Función para fusionar runs utilizando un heap
def merge_runs(runs):
    merged_result = []
    heap = [(run[0], i, 0) for i, run in enumerate(runs) if run]
    heapq.heapify(heap)
    
    while heap:
        val, run_idx, ele_idx = heapq.heappop(heap)
        merged_result.append(val)
        
        ele_idx += 1
        if ele_idx < len(runs[run_idx]):
            heapq.heappush(heap, (runs[run_idx][ele_idx], run_idx, ele_idx))
    
    return merged_result

# Función principal para la distribución de initial runs
def distribute_initial_runs(arr, k):
    # Dividir la lista en runs iniciales
    runs = split_into_runs(arr, k)
    
    # Ordenar cada run individualmente
    sorted_runs = sort_runs(runs)
    
    # Fusionar los runs ordenados
    sorted_arr = merge_runs(sorted_runs)
    
    return sorted_arr

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7, 1, 3, 8]
k = 3  # Tamaño de los runs iniciales

print("Lista original:", arr)

# Aplicar el método de distribución de initial runs
sorted_arr = distribute_initial_runs(arr, k)

print("Lista ordenada:", sorted_arr)
