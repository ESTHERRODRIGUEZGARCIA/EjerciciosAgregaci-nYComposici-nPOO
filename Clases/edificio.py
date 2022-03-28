# al día siguiente:

from numpy import append


class empresa():
    def __init__(self, nombre) -> None: #constructor
        self.nombre = nombre


class edificio():
    pass

class ciudad():


    pass

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