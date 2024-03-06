def buscar_elemento(lista, objetivo):
    for num in lista:
        if num == objetivo:
            return True
    return False
#Ejemplo de uso
lista = [23, 4, 56, 7, 8, 9, 12]
objetivo = 8
print("el numero ", objetivo, "esta presente en el arreglo? ", buscar_elemento(lista, objetivo))