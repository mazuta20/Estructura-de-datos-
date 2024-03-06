def buscar_elemento(lista, lista2):
    for elem in lista:
        if elem in lista2:
            return True
    return False

lista = [23, 4, 56, 7, 8, 9, 12]
lista2 = [8,6]
print( buscar_elemento(lista, lista2))