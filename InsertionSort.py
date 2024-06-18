"""Dafne Villanueva
Este código muestra cómo funciona el algoritmo de inserción para ordenar una lista de números, explicando cada paso con comentarios detallados."""

def insertion_sort(arr):
    # Iteramos desde el segundo elemento hasta el final de la lista
    for i in range(1, len(arr)):
        # La 'clave' es el elemento actual que queremos insertar en la sublista ordenada
        key = arr[i]
        
        # Inicializamos j para que sea el índice del elemento anterior al actual
        j = i - 1
        
        # Desplazamos los elementos de la sublista ordenada que son mayores que la 'clave'
        # hacia la derecha, para hacer espacio para la 'clave'
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertamos la 'clave' en su posición correcta en la sublista ordenada
        arr[j + 1] = key
    
    # Devolvemos la lista ordenada
    return arr

# Ejemplo de uso
lista = [4, 3, 2, 10, 12, 1, 5, 6]

# Llamamos a la función de ordenación por inserción y almacenamos el resultado en 'ordenada'
ordenada = insertion_sort(lista)

# Imprimimos la lista ordenada
print(ordenada)
