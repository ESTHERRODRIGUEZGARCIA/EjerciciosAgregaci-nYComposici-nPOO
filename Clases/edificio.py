# al día siguiente:

from numpy import append


class ciudad():

    def __init__(self, nombre, city) -> None:
        self.empres = empresa(nombre)
        self.city = city

class empresa():
    def __init__(self, nombre) -> None: #constructor
        self.nombre = nombre




class empleados():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    pass

emp = empresa("YooHoo")
lista_empleados = ["Martin", "Salim"]
lista = []
for nombre in lista_empleados:
    empleado = empleados(nombre)
    lista.append(empleado)