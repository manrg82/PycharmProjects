from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"{super().__str__()}\nCuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Deposito aceptado")

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")