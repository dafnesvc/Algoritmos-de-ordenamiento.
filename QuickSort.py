"""Dafne Villanueva 21310176
QuickSort--->Este código implementa el algoritmo QuickSort en Python, utilizando las funciones partition para dividir el array y quick_sort 
para la recursión y ordenación"""


def partition(arr, low, high):
    # Tomamos el último elemento como el pivote
    pivot = arr[high]
    
    # Índice del elemento más pequeño
    i = low - 1
    
    # Recorremos todos los elementos del array
    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            # Incrementamos el índice del elemento más pequeño
            i += 1
            # Intercambiamos arr[i] con arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Intercambiamos arr[i + 1] con arr[high], para colocar el pivote en su lugar correcto
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Devolvemos el índice donde el pivote está actualmente ubicado
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Obtener el índice de partición
        pi = partition(arr, low, high)
        
        # Ordenar los elementos antes y después de la partición
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Ejemplo de uso
lista = [10, 7, 8, 9, 1, 5]
n = len(lista)
print("Lista original:", lista)

# Llamamos a la función quick_sort para ordenar la lista
quick_sort(lista, 0, n - 1)

# Imprimimos la lista ordenada
print("Lista ordenada:", lista)
