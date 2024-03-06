if __name__ == '__main__':
    mi_lista=[3,4,7,9,10,15]
    def suma_lista(lista):
        suma = 0
        for elem in lista:
            suma += elem
        return suma
    resultado = suma_lista(mi_lista)
    print("La suma de los elementos en la lista es:", resultado)