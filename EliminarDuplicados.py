if __name__ == '__main__':
    lista = [1, 3, 4, 1, 2, 3, 4, 7, 6]

    def duplicado(lista):
        for i in lista:
            if lista.count(i) > 1:
                lista.remove(i)
        return lista
    mi_lista = duplicado(lista)
    print(mi_lista)
