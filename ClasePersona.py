class persona:
    def __init__(self,nombre,edad,genero):
        self.nombre= nombre
        self.edad = edad
        self.genero = genero

    def hablar(self):
        print( f"{self.nombre} esta 'hablando!' ")

class empleado(persona):
    def __init__(self, salario, puesto_trabajo, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        self.salario = salario
        self.puesto = puesto_trabajo

    def hablar(self):
        return f"{self.nombre} esta 'hablando!' "
class estudiante(persona):
    def __init__(self, escula , grado):
        self.escuela = escula
        self.grado = grado



# se crea instacia de subclase
Estudiante = estudiante("u-caldas", 11)
empl = empleado(120000, "auxiliar", "mateo ", 24 , "masculino")
print(f"la persona se llama {empl.nombre} y tiene {empl.edad} años y su genero es {empl.genero}, el es {empl.puesto} y su salario es  {empl.salario} el esta estudiando en {Estudiante.escuela} y esta en grado{Estudiante.grado}")
empl.hablar()


