# al día siguiente:

from numpy import append


class ciudad():
    class empresa():
        def __init__(self, nombre) -> None: #constructor
            self.nombre = nombre

    def __init__(self, nombre) -> None:
        self.empres = self.empresa(nombre)

    pass
class edificio():

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