if __name__ == '__main__':
    lista = [23, 4, 56, 7, 8, 9, 12]

    def ordenamiento_seleccion(my_lista):
        for i in range(len(my_lista)-1):
            menor = i
            for n in range(1+i,len(my_lista)):
                if my_lista[n] < my_lista[menor]:
                    menor=n
            if menor !=i:
                my_lista[menor], my_lista[i]= my_lista[i], my_lista[menor]
    ordenamiento_seleccion(lista)
    print(lista)