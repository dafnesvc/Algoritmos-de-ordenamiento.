"""Dafne Villanueva 21310176
Straight Merging--->El método Straight Merging, también conocido como Simple Merge Sort o Iterative Merge Sort, es un algoritmo iterativo 
que utiliza una combinación de iteración y fusión para ordenar un array. """

def straight_merge(arr, left, middle, right):
    # Definimos las subsecuencias izquierda y derecha
    n1 = middle - left + 1
    n2 = right - middle
    
    L = arr[left:left + n1]    # Subsecuencia izquierda
    R = arr[middle + 1:right + 1]  # Subsecuencia derecha
    
    i = j = 0   # Inicializamos los índices para L y R
    k = left    # Inicializamos el índice para arr
    
    # Combinamos las subsecuencias L y R en arr
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Si quedan elementos en L, los añadimos a arr
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Si quedan elementos en R, los añadimos a arr
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr):
    current_size = 1    # Tamaño actual de los subarrays a fusionar
    
    # Iteramos sobre el tamaño de los subarrays a fusionar
    while current_size < len(arr) - 1:
        left = 0
        
        # Fusionamos subarrays de tamaño current_size
        while left < len(arr) - 1:
            middle = left + current_size - 1
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])
            
            # Llamamos a la función straight_merge para fusionar los subarrays
            straight_merge(arr, left, middle, right)
            left += current_size * 2
        
        current_size = 2 * current_size

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Lista original:", arr)

# Llamamos a la función merge_sort para ordenar la lista
merge_sort(arr)

# Imprimimos la lista ordenada
print("Lista ordenada:", arr)
