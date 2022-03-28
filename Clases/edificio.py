# al día siguiente:

ciudad = str(input("¿Qué ciudad quiere que sea destrozada, NY / LA? "))
edificios = ["A", "B", "C"] # añadir destruidos
empleados = ["Martin", "Salim", "Sra. Xing"] #añadir muertos
class Edificio():
    def __init__(self, nombre, numero_plantas) -> None:
        self.n = nombre
        self.plantas = numero_plantas
