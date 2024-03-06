def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos del arreglo
    for i in range(n):
        # Los últimos i elementos ya están en posición
        for j in range(0, n-i-1):
            # Recorrer el arreglo desde 0 hasta n-i-1
            # Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")