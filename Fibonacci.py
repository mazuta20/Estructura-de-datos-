if __name__ == '__main__':
    a = 0
    b = 1
    i = 0
    print(a)

    for i in range(10):
        a_guardado = a
        a = b
        b = a_guardado + b

        print(a)
        i = i + 1