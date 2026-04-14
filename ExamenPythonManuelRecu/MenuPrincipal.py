from os.path import exists
from random import Random, randint

from Cuenta import Cuenta
def crearArchivo():#aqui creo el archivo y le escribo las cuentas por defecto
    cuentasejemplo={
        '1234567890;Ana Lopez;850.5',
        '9876543210;Juan Pérez;1200.00',
        '5550011122;Lucía Martin;300.00',
    }
    archivo = open('cuentas.csv', 'w')
    for cuenta in cuentasejemplo:
       archivo.write(cuenta + "\n")
    archivo.close()
def txtMenuPrincipal():
    print("=== SISTEMA DE CUENTAS BANCARIAS ===")
    print("1) Listar Cuentas")
    print("2) Crear Nueva Cuenta")
    print("3) Seleccionar cuenta por número")
    print("4) Guardar y salir")
def txtSubMenu():
    print("a) Consultar saldo")
    print("b) Ingresar Dinero")
    print("c) Retirar Dinero")
    print("d) Salir")
def leerCuentasdeArchivo():#leo cuentas del archivo csv usando split y creando objetos cuenta que meto en la lista que devuelvo
    lsCuentas=[]
    archivo = open('cuentas.csv')
    cuentas=archivo.readlines()
    for c in cuentas:
        c.split(';')
        lsCuentas.append(Cuenta(c[0],c[1],c[2]))
    return lsCuentas
def listarCuentas(listaCuentas):#recibo la lista de cuentas y la voy leyendo
    for cuenta in listaCuentas:
        print(cuenta.getNumero()+" | Titular: "+cuenta.getTitular())
def escribirCuenta(tt,sl):#creo una cuenta con un numero de cuenta al azar entre 0000000000 y 9999999999
    archivo = open('cuentas.csv','a')
    archivo.write(str(randint(0000000000,9999999999))+";"+str(tt)+";"+str(sl)+"\n")
def encontrarCuentaPorNum(nm): #encuentro una cuenta en el archivo por su numero de cuenta
    lsCuentas = []
    archivo = open('cuentas.csv')
    cuentas = archivo.readlines()
    for c in cuentas:
        c.split(';')
        lsCuentas.append(Cuenta(c[0], c[1], c[2]))
    for cuenta in lsCuentas:
        if cuenta.getNumero()==nm:
            return Cuenta(cuenta[0],cuenta[1],cuenta[2])
    return None

def subMenu(cuenta):
    txtSubMenu()
    cuenta.__class__=Cuenta
    opcion = input("Ingrese su opcion: ")
    match opcion:
        case ('a'):
            print("Saldo de la cuenta: "+cuenta.getSaldo())
            subMenu(cuenta)
        case ('b'):
            cantidad = int(input("Ingrese la cantidad a ingresar: "))
            print("Saldo de la cuenta: "+cuenta.saldo())
            subMenu(cuenta)
        case ('c'):
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if(cuenta.retirar(cantidad)==1):
                print("Saldo de la cuenta: "+cuenta.getSaldo())
            else:
                print("Cantidad invalida")
            subMenu(cuenta)
        case ('d'):
            print("Volviendo al menu principal")
            return
        case _:
            print("Opcion no valida")
            subMenu(cuenta)
def menuPrincipal():
    listaCuentas=leerCuentasdeArchivo()
    txtMenuPrincipal()
    opcion= int(input("Ingrese su opcion: "))
    match opcion:
        case (1):
            listarCuentas(listaCuentas)
            menuPrincipal()
        case (2):
            tt= input("Titular de Cuenta : ")
            sl= input("Saldo de Cuenta : ")
            escribirCuenta(tt,sl)
            print("Cuenta creada exitosamente")
            menuPrincipal()
        case (3):
            nm= int(input("Numero de Cuenta : "))
            archivo = open('cuentas.csv', 'r')
            cuentas = archivo.readlines()
            cu=None
            for c in cuentas:
                cuenta = c.split(';')
                if cuenta[0] == nm:
                    subMenu(Cuenta(cuenta[0], cuenta[1], cuenta[2]))
            menuPrincipal()
        case (4):
            print("Guardando cambios, hasta pronto...")
            return
        case _:
            print("Opcion no valida")
            menuPrincipal()


crearArchivo()
menuPrincipal()