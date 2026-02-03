class Cuenta:
    #atributos
    numero=0
    titular=""
    saldo=0

    def __init__(self,nm,tt,sl):#constructor
        self.numero = nm
        self.titular = tt
        self.saldo = sl

    #getters
    def getSaldo(self):
        return self.saldo

    def getNumero(self):
        return self.numero

    def getTitular(self):
        return self.titular

    #ingresar en cuenta
    def ingresar(self,cantidad):
        if cantidad is float|int:
            self.saldo += cantidad
            return 1
        else:
            return 0

    def retirar(self,cantidad):#retirar en cuenta
        if (cantidad is float|int):
            if(cantidad < self.saldo):
                self.saldo -= cantidad
                return 1
            else:
                raise ValueError("La cantidad es mayor que el numero")#lanzo excepcion si la cantidad a restar es mayor que el saldo actual
        else:
            return 0