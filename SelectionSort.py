"""Dafne Villanueva 
 Selección (SelectionSort).-->Este código muestra cómo funciona el algoritmo de selección para ordenar una lista de números"""


def selection_sort(arr):
    # Iteramos sobre cada elemento del array
    for i in range(len(arr)):
        # Suponemos que el primer elemento no ordenado es el menor
        min_index = i
        
        # Iteramos sobre los elementos restantes no ordenados
        for j in range(i + 1, len(arr)):
            # Si encontramos un elemento menor, actualizamos el índice del mínimo
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiamos el elemento actual con el elemento más pequeño encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Imprimimos el estado del array en cada paso (opcional para depuración)
        print(f"Paso {i+1}: {arr}")
    
    # Devolvemos el array ordenado
    return arr

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]

# Llamamos a la función de ordenación por selección y almacenamos el resultado en 'ordenada'
ordenada = selection_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", ordenada)
