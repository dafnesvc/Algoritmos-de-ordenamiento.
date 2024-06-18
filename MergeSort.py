"""Dafne Villanueva 21310176
MergeSort---> Este código implementa el algoritmo Merge Sort en Python, utilizando las funciones merge_sort para la recursión y merge 
para combinar y ordenar las sublistas"""


def merge_sort(arr):
    # Si la longitud del array es menor o igual a 1, está ordenado por definición
    if len(arr) <= 1:
        return arr
    
    # Calculamos el punto medio del array
    mid = len(arr) // 2
    
    # Dividimos el array en mitades izquierda y derecha
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Llamamos recursivamente a merge_sort para ordenar cada mitad
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinamos las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    # Inicializamos un array vacío para almacenar el resultado combinado
    merged = []
    
    # Índices para recorrer las mitades izquierda y derecha
    i = j = 0
    
    # Combinamos las dos mitades en orden ascendente
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Agregamos los elementos restantes de la mitad izquierda (si los hay)
    merged.extend(left[i:])
    
    # Agregamos los elementos restantes de la mitad derecha (si los hay)
    merged.extend(right[j:])
    
    # Devolvemos el array combinado y ordenado
    return merged

# Ejemplo de uso
lista = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista)

# Llamamos a la función merge_sort para ordenar la lista
ordenada = merge_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", ordenada)
