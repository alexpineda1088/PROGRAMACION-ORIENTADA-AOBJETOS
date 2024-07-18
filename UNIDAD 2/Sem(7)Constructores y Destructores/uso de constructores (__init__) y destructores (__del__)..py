class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):

       #Constructor de la clase CuentaBancaria.
        #Inicializa los atributos titular y saldo.

        #:param titular: Nombre del titular de la cuenta.
        #:param saldo_inicial: Saldo inicial de la cuenta.

        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con saldo inicial de {self.saldo}.")

    def depositar(self, monto):

        #Deposita una cantidad en la cuenta.

        #:param monto: Cantidad a depositar.

        self.saldo += monto
        print(f"Depositados {monto}. Saldo actual: {self.saldo}.")

    def retirar(self, monto):

        #Retira una cantidad de la cuenta.

        #:param monto: Cantidad a retirar.

        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retirados {monto}. Saldo actual: {self.saldo}.")
        else:
            print("Fondos insuficientes.")

    def __del__(self):

        #Destructor de la clase CuentaBancaria.
       # Imprime un mensaje indicando que la cuenta está siendo cerrada.

        print(f"La cuenta de {self.titular} ha sido cerrada.")


class Transaccion:
    def __init__(self, cuenta_origen, cuenta_destino, monto):

        #Constructor de la clase Transaccion.
        #Inicializa los atributos cuenta_origen, cuenta_destino y monto.

        #:param cuenta_origen: Cuenta de origen de la transacción.
        #:param cuenta_destino: Cuenta de destino de la transacción.
        #:param monto: Monto de la transacción.

        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.monto = monto
        print(f"Transacción creada de {self.monto} de {self.cuenta_origen.titular} a {self.cuenta_destino.titular}.")

    def ejecutar(self):

       # Ejecuta la transacción transfiriendo el monto de la cuenta de origen a la cuenta de destino.

        if self.cuenta_origen.saldo >= self.monto:
            self.cuenta_origen.retirar(self.monto)
            self.cuenta_destino.depositar(self.monto)
            print("Transacción completada.")
        else:
            print("Transacción fallida. Fondos insuficientes en la cuenta de origen.")

    def __del__(self):

       #Destructor de la clase Transaccion.
        #Imprime un mensaje indicando que la transacción está siendo destruida.

        print(
            f"La transacción de {self.monto} de {self.cuenta_origen.titular} a {self.cuenta_destino.titular} ha sido destruida.")


# Demostración del uso de constructores y destructores

# Crear cuentas bancarias
cuenta1 = CuentaBancaria('Ana', 1000)
cuenta2 = CuentaBancaria('Carlos', 500)

# Realizar una transacción
transaccion = Transaccion(cuenta1, cuenta2, 300)
transaccion.ejecutar()
# La transacción será destruida automáticamente al final del programa

# Los objetos CuentaBancaria serán destruidos automáticamente al final del programa
