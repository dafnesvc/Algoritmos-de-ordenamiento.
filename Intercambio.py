""""Dafne Villanueva 21310176
Intercambio--> Conocido como Bubble Sort (ordenación de burbuja), es un algoritmo simple de ordenación que repite repetidamente a través de 
la lista, comparando y, si es necesario, intercambiando elementos adyacentes.
Este código muestra cómo funciona el algoritmo de intercambio (Bubble Sort) para ordenar una lista de números"""

def bubble_sort(arr):
    # Obtenemos la longitud de la lista
    n = len(arr)
    
    # Iteramos sobre cada elemento de la lista
    for i in range(n):
        # Esta variable se usa para optimización; si no hubo intercambio, la lista ya está ordenada
        swapped = False
        
        # Iteramos sobre la lista desde el primer elemento hasta el n-i-1
        # Los últimos i elementos ya estarán en su posición correcta
        for j in range(0, n-i-1):
            # Comparamos el elemento actual con el siguiente
            if arr[j] > arr[j+1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Indicamos que ha habido un intercambio
                swapped = True
        
        # Imprimimos el estado de la lista después de cada pasada (opcional para depuración)
        print(f"Paso {i+1}: {arr}")
        
        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not swapped:
            break
    
    # Devolvemos la lista ordenada
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]

# Llamamos a la función de ordenación por burbuja y almacenamos el resultado en 'ordenada'
ordenada = bubble_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", ordenada)
