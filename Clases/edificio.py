# al día siguiente:

ciudad = str(input("¿Qué ciudad quiere que sea destrozada, NY / LA? "))
edificios = ["A", "B", "C"] # añadir destruidos
empleados = ["Martin", "Salim", "Sra. Xing"] #añadir muertos
class Edificio():
    def __init__(self, nombre, numero_plantas) -> None:
        self.n = nombre
        self.plantas = numero_plantas
class Empleado():
    pass

class Empresa(): #
    pass

class Ciudad():
    pass

class NewYork():
    def __del__(self):
        print("Destrucción edificio de Nueva York.")

class LosAngeles():
    def __del__(self):
        print("Destrucción edificio de LosÁngeles.")


edificio = Edificio("hola", 23)
edificio.getNombre()
edificio.n = "res"
edificio.setNombre("res")