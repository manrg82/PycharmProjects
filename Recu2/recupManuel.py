import os
import random
from os.path import split
from random import Random

ARCHIVO='tareas.txt'
class Tarea:
    id: int
    descripcion: str
    estado: bool
    def __init__(self, id: int, desc: str, est: bool) -> None:
        self.id = id
        self.descripcion = desc
        self.estado = est
    def getId(self) -> int:
        return self.id
    def getDescripcion(self) -> str:
        return self.descripcion
    def getEstado(self) -> bool:
        return self.estado
    def completarTarea(self) -> None:
        self.estado = True
    def mostrar(self) -> None:
        print(self.id)
        print(self.descripcion)
        print(self.estado)
def guardar_datos(lista):
    #escribo la lista de tareas en el archivo para guardar
    try:
        with open(ARCHIVO, 'w') as f:
            for t in lista:
                f.write(f"{t.getId()};{str(t.getDescripcion())};{t.getEstado()}\n")
    except IOError as e:
        print(f"Error al guardar los datos: {e}")
def inicializarArchivo() -> None:
    if not os.path.exists(ARCHIVO):#compruebo si existe el fichero y si no creo 3 objetos tarea y los escribo
        t1=Tarea(1,"desc1",False)
        t2 = Tarea(2, "desc2", False)
        t3 = Tarea(3, "desc3", False)
        try:
            with open(ARCHIVO, 'w') as f:
                f.write(f"{t1.getId()};{t1.getDescripcion()};False\n")
                f.write(f"{t2.getId()};{t2.getDescripcion()};False\n")
                f.write(f"{t3.getId()};{t3.getDescripcion()};False\n")
            print("Archivo creado con datos de prueba.")
        except IOError as e:
            print(f"Error al crear el archivo: {e}")
def leerTareas():
    #cargo la lista de tareas desde el archivo
    listaTareas = []
    try:
        with open(ARCHIVO, 'r') as f:
            for linea in f:
                partes = linea.strip().split(';')
                if len(partes) == 3:
                    nueva = Tarea(int(partes[0]), partes[1],partes[2])
                    listaTareas.append(nueva)
    except Exception as e:
        print(f"Error al leer los datos: {e}")
    return listaTareas

def menu_principal():
    inicializarArchivo()
    listaTareas = leerTareas()
    while True:
        indiceTareas= len(listaTareas)#indice para saber cuantas tareas existen en el archivo, se actualiza cuando se crea una tarea nueva o cuando se cargan de nuevo del archivo
        print("=== GESTOR DE TAREAS ===")
        print("1) Listar Tareas")
        print("2) Añadir Tarea")
        print("3) Marcar Tarea como completada")
        print("4) Mostrar tarea aleatoria del día")
        print("5) Guardar y salir")
        try:
            opcion: int= int(input("Seleccione una opción: "))
            match opcion:
                case(1):
                    print("LISTA DE TAREAS")
                    for t in listaTareas:
                        print(f"ID: {t.getId()}, DESCRIPCION: {t.getDescripcion()}, COMPLETADO: {t.getEstado()}.")#alternativamente se puede usar el metodo mostrar() dentro de la clase, pero aqui he decidido mostrarlo asi para que ponga un texto antes de cada atributo y probar el printf
                case(2):
                    print("AÑADIR UNA NUEVA TAREA:")
                    descripcion: str = input("Descripcion: ")
                    tareaNueva: Tarea=Tarea(indiceTareas+1,descripcion,False)
                    listaTareas.append(tareaNueva)
                    indiceTareas+=1
                case(3):
                    print("COMPLETAR UNA DE LAS SIGUIENTES TAREAS:")
                    for t in listaTareas:
                        print(f"    ID: {t.getId()}, DESCRIPCION: {t.getDescripcion()}, COMPLETADO: {t.getEstado()}.")
                    opt: int= int(input("Introduce una tarea que quieras completar: "))
                    listaTareas[opt-1].completarTarea()#hago indice -1 para no salir de la capacidad
                    print("LISTA DE TAREAS ACTUALIZADA: ")
                    for t in listaTareas:
                        print(f"    ID: {t.getId()}, DESCRIPCION: {t.getDescripcion()}, COMPLETADO: {t.getEstado()}.")
                case(4):
                    rand:int
                    listaPendientes=[]#hago una lista con las tareas que estan pendientes para ver si hay, si no hay return
                    for t in listaTareas:
                        if str(t.getEstado())=="False":
                            listaPendientes.append(t)
                    if len(listaPendientes)==0:
                        print("TODAS LAS TAREAS COMPLETADAS")
                        return
                    rand=random.randint(0,len(listaPendientes)-1)
                    print("TAREA AL AZAR: ")
                    listaPendientes[rand].mostrar()#muestro con el metodo custom
                case(5):
                    guardar_datos(listaTareas)#escribo datos al fichero
                    print("DATOS GUARDADOS, HASTA PRONTO")
                    return
                case(_):
                    print("ERROR")
                    return
        except ValueError as e:
            print(f"Error al recibir la opcion: {e}")
menu_principal()