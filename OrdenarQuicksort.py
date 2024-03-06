if __name__ == '__main__':
    lista = [23, 4, 56, 7, 8, 9, 12]
    def QuickSort(numeros, izq, der):

        pivote = numeros[izq]
        i = izq
        j = der
        aux = 0

        while i < j:
            while numeros[i] <= pivote and i < j:
                i += 1

            while numeros[j] > pivote:
                j -= 1

            if i < j:
                aux = numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = aux

        numeros[izq] = numeros[j]
        numeros[j] = pivote

        if izq < j - 1:
            QuickSort(numeros, izq, j - 1)

        if j + 1 < der:
            QuickSort(numeros, j + 1, der)

    QuickSort(lista, 0, len(lista) - 1)
    print(lista)