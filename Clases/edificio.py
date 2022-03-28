# al día siguiente:

from numpy import append


class ciudad():

    def __init__(self, nombre_empresa, city, lista_empleados) -> None:
        self.empres = empresa(nombre_empresa, lista_empleados)
        self.city = city


class empresa():
    def __init__(self, nombre_empresa, lista_empleados) -> None: #constructor
        self.nombre_empresa = nombre_empresa
        self.lista_empleados = []

        for i in lista_empleados:
            empleado = empleados(i)
            self.lista_empleados.append(empleado)




class empleados():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    pass

lista_empleados = ["Martin", "Salim", "Xing"]

ciudad1 = ciudad("A", "NY1", lista_empleados)
ciudad2 = ciudad("B", "NY2", lista_empleados)
ciudad3 = ciudad("C", "LA", lista_empleados)

