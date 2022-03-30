# EjerciciosAgregaciónYComposiciónPOO
En este repositorio se encuentran resueltos los ejercicios de Agregación y Composición de POO. Entrega Individual: UML Y CÓDIGO

Enlace del repositorio: https://github.com/ESTHERRODRIGUEZGARCIA/EjerciciosAgregaci-nYComposici-nPOO.git


# a. El día siguiente
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.

````
# al día siguiente:

from time import sleep
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
    def getempleados(self):
        for i in self.lista_empleados:
            print(i.nombre)


def eliminarciudad(ciudad_eliminada):
    for i in lista_ciudades:
        if ciudad_eliminada == i.city:
            del(i)




class empleados():
    def __init__(self, nombre) -> None:
        self.nombre = nombre

lista_empleados = ["Martin", "Salim", "Xing"]

ciudad1 = ciudad("A", "NY1", lista_empleados)
ciudad2 = ciudad("B", "NY2", lista_empleados)
ciudad3 = ciudad("C", "LA", lista_empleados)
lista_ciudades = [ciudad1, ciudad2, ciudad3]

ciudad_eliminada = str(input("¿Qué ciudad desea eliminar? LA NY1 NY2"))

eliminarciudad(ciudad_eliminada)

````

UML:
![image](https://user-images.githubusercontent.com/91721860/160932915-b33c487d-0238-439b-aab2-ae4287807a2e.png)


# b. ¿Inmortal?
Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?

````
class Yin: pass 
class Yang: 
    def __del__(self): # atributo privado
        print("Yang destruido") 
 
yin = Yin()
yang = Yang()
yin.yang = yang #eliminar

print(yang) 
del(yin.yang)
del(yang) 

print("?")

#nos devuelve Yang destruido ?
# salta "yang" pues no se le hace referencia

````

![image](https://user-images.githubusercontent.com/91721860/160933379-403c1da5-19f4-49d1-be17-07cf70819489.png)


# c. Alternativa a la herencia múltiple
En el último ejercicio de la sección sobre la herencia, se mostraron los límites de la herencia múltiple: acoplamientos de clases cuyo vínculo no es tan obvio, atajos tomados en el código que tienen mucho riesgo de error. Este ejercicio utiliza otro enfoque del problema: la asociación (ya sea composición o agregación). 

Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.

Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.

Enunciado: modifique el código para que el programa funcione de nuevo.

````
casa = {}
orientaciones = ['NORTE', 'SUR', 'ESTE', 'OESTE']

class interfaz_cristal():
  global casa
  def Paredes(self, orientacion):
    for i in range(len(orientacion)):
      nombre = orientacion[i]
      casa[nombre] = {
          'ventanas': {},
      }
    print(casa)
    interfaz_cristal().Ventanas([['NORTE', 0.5, ''], ['SUR', 1, ''], ['ESTE', 2, ''], ['OESTE', 1, '']])
  def Ventanas(self, ventanas):
    dimensiones = []
    for i in range(len(ventanas)):
      nombre = ventanas[i][0]
      casa[nombre]['ventanas'] = {
        'superficie': ventanas[i][1],
        'proteccion': ventanas[i][2]
      }
      dimensiones.append(ventanas[i][1])  
    print(casa)
    interfaz_cristal().Superficie()
  def Superficie(self):
    total = 0
    for i in range(len(orientaciones)):
      total += casa[orientaciones[i]]['ventanas']['superficie']
    print('Superficie acristalada: ' + str(total))
  def ParedCortina(self, orientacion, tamaño):
    casa[orientacion]['ventanas']['superficie'] += tamaño
    print(casa)
  def ComprobarProteccion(self, orientacion):
    if casa[orientacion]['ventanas']['proteccion'] != '':
      print('Protección en regla.')
    else:
      print('Protección obligatoria no presente.')

   ````

   
![image](https://user-images.githubusercontent.com/91721860/160934128-bb6372c3-ae86-4146-b927-eedfecba57f9.png)

