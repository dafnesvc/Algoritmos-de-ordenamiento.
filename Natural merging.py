"""Dafne Villanueva 21310176
Natural merging--->El algoritmo primero encuentra las subsecuencias ordenadas en la lista original (find_runs), luego las fusiona iterativamente hasta
que toda la lista esté ordenada (merge y natural_merge_sort)."""


def natural_merge_sort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    # Función para encontrar subsecuencias ordenadas (runs)
    def find_runs(arr):
        runs = []
        start = 0
        
        while start < len(arr):
            end = start + 1
            while end < len(arr) and arr[end] >= arr[end - 1]:
                end += 1
            runs.append(arr[start:end])
            start = end
        
        return runs
    
    # Función para fusionar dos subsecuencias ordenadas
    def merge(arr, left, middle, right):
        L = arr[left:middle + 1]
        R = arr[middle + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    # Encontramos y fusionamos las subsecuencias ordenadas
    runs = find_runs(arr)
    sorted_arr = arr[:]
    
    while len(runs) > 1:
        temp_runs = []
        i = 0
        
        while i < len(runs) - 1:
            merge(sorted_arr, 0, len(runs[i]) - 1, len(runs[i]) + len(runs[i + 1]) - 1)
            temp_runs.append(sorted_arr[:len(runs[i]) + len(runs[i + 1])])
            sorted_arr = sorted_arr[len(runs[i]) + len(runs[i + 1]):]
            i += 2
        
        if i == len(runs) - 1:
            temp_runs.append(runs[-1])
        
        runs = temp_runs
    
    arr[:] = temp_runs[0] if temp_runs else sorted_arr

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7, 1, 3, 8]
print("Lista original:", arr)

natural_merge_sort(arr)

print("Lista ordenada:", arr)

