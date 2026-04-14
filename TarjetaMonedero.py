class TarjetaMonedero:
    def __init__(self, numero, propietario, saldo):
        self.numero = numero
        self.propietario = propietario
        self.__saldo = float(saldo)
    def get_numero(self):
        return self.numero
    def get_propietario(self):
        return self.propietario
    def get_saldo(self):
        return self.__saldo
    def recargar(self, cantidad):
        if cantidad >= 0:
            saldo = self.get_saldo()
            saldo += cantidad

    def pagar(self, cantidad):
        if cantidad > 0:
            saldo = self.get_saldo()
            saldo += cantidad
