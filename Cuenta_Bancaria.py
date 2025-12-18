# Control básico de una cuenta bancaria
class CuentaBancaria:
    # Costructor
    def __init__(self, nombre_del_titular, saldo_inicial):
        self.nombre_del_titular = nombre_del_titular
        self.saldo_inicial = saldo_inicial
    
    # Metodo
    def mostrar_info(self):
        print(f"Hola, {self.nombre_del_titular} su saldo actual es de ${self.saldo_inicial} Pesos ")

    # Metodo
    def depositar(self, cantidad):
        self.saldo_inicial = self.saldo_inicial + cantidad

    # Metodo
    def retirar(self, cantidad):
        if self.saldo_inicial <= cantidad:
         print("No cuenta con suficiente saldo para retirar")
        else:  
            self.saldo_inicial = self.saldo_inicial - cantidad

cuenta1 = CuentaBancaria("Juan Perez", 2000)
cuenta2 = CuentaBancaria("Jose Perez",500)

cuenta1.depositar(250)
cuenta1.retirar(100)

cuenta2.depositar(320)
cuenta2.retirar(1000)

print(cuenta1.mostrar_info())
print("-----------------------------------")
print(cuenta2.mostrar_info())
