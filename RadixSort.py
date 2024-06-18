"""Dafne Villanueva 21310176
RadixSort---> Este código implementa el algoritmo Radix Sort en Python, utilizando las funciones counting_sort para ordenar los elementos
en función de los dígitos y radix_sort para manejar los diferentes dígitos del número"""

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Array de salida que almacenará los elementos ordenados
    count = [0] * 10  # Array para almacenar el conteo de elementos de 0-9 en exp-th place
    
    # Calculamos el conteo de cada dígito en exp-th place
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Calculamos las posiciones reales de los elementos en output
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construimos el array de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copiamos el array de salida a arr[], para que arr[] contenga los números ordenados según el dígito actual
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontramos el número máximo para saber el número de dígitos
    max_num = max(arr)
    
    # Aplicamos counting sort a cada dígito. exp es 10^i donde i es el dígito actual que se está procesando
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", lista)

# Llamamos a la función radix_sort para ordenar la lista
radix_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", lista)
