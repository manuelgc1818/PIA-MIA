class CuentaBancaria:

    def __init__(self, titular, saldo=0.0):

        self.titular = titular

        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def retirar(self, cantidad):
        if cantidad > self._saldo:
            raise ValueError("pobre.")
        self._saldo -= cantidad



cuenta = CuentaBancaria("mia", 1)
cuenta.retirar(1)
print(cuenta.saldo)
cuenta.retirar(1)  

