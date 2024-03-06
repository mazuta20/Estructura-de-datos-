class rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho


    def area(self):
        area = self.longitud * self.ancho
        return area
    def perimetro(self):
        perimetro = 2 *(self.longitud + self.ancho)
        return perimetro

el_rectanfulo = rectangulo(4,6)

area_rectangulo = el_rectanfulo.area()
perimetro_rectangulo = el_rectanfulo.perimetro()
print("el area del rectangulo es ",area_rectangulo, "y el perimetro es", perimetro_rectangulo)

