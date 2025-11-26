from clases.Cliente import Cliente

def crear_cliente():
    nombre_in = input("Ingrese su nombre: ")
    apellido_in = input("Ingrese su apellido: ")
    cuenta_in = input("Ingrese numero de cuenta: ")
    return Cliente(nombre_in, apellido_in, cuenta_in)


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = 0
    while opcion != 3:
        print("\n--- MENU ---")
        print("[1] Depositar")
        print("[2] Retirar")
        print("[3] Salir")

        try:
            opcion = int(input("Elija una opcion: "))
        except ValueError:
            print("Por favor ingrese un numero valido")
            continue

        if opcion == 1:
            monto_dep = float(input("Cuanto desea depositar?: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 2:
            monto_ret = float(input("Cuanto desea retirar?: "))
            mi_cliente.retirar(monto_ret)
        elif opcion == 3:
            print("Gracias por usar nuestro banco")

        if opcion != 3:
            print(mi_cliente)


if __name__ == "__main__":
    inicio()