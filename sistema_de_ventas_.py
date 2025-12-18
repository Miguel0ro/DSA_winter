#Problema: Sistema básico de ventas por vendedor

#Contexto

#Una empresa desea llevar el control de sus vendedores y las ventas realizadas por cada uno durante el día. Cada vendedor tiene múltiples ventas registradas y se necesita obtener información básica a partir de estos datos.

#---

#Estructura de datos esperada

#Se utilizará un diccionario donde:

#Clave: nombre del vendedor (string).

#Valor: lista de montos de ventas (lista de números).

#---

#Instrucciones

#1. Crea una clase llamada SistemaVentas.

#2. La clase debe tener:

#Un constructor que inicialice un diccionario vacío de vendedores.

#Un método agregar_vendedor que reciba el nombre del vendedor y lo agregue al sistema con una lista vacía de ventas.

#Un método registrar_venta que reciba el nombre del vendedor y el monto de la venta, y agregue el monto a su lista correspondiente.

#Un método mostrar_ventas que muestre cada vendedor con todas sus ventas.

#Un método total_vendedor que reciba el nombre de un vendedor y muestre el total de ventas realizadas (calculado manualmente).

3
#Un método mejor_vendedor que determine y muestre el nombre del vendedor con mayor total de ventas.

#3. En el programa principal:

#Registra varios vendedores.

#Agrega múltiples ventas a cada vendedor.

#Muestra todas las ventas.

#Muestra el vendedor con mayores ventas.

class SistemaVentas:
    def __init__(self):
        self.vendedores = {}

    def agregar_vendedor(self, nombres):
        self.vendedores[nombres] = []

    def registrar_venta(self, nombre, monto):
        if nombre in self.vendedores:
            self.vendedores[nombre].append(monto)
        else:
            print(f"El vendedor {nombre} no existe")

    def mostrar_ventas(self):
        for vendedor, ventas in self.vendedores.items():
            print(f"Vendedor: {vendedor}")
            print("Ventas:", ventas)
            print()

    def total_vendedor(self, nombre):
        if nombre in self.vendedores:
            total = 0
            for venta in self.vendedores[nombre]:
                total += venta
            print(f"Total de ventas de {nombre}: ${total}")
            return total
        else:
          
            return 0

    def mejor_vendedor(self):
        mejor = None
        mayor_total = 0

        for vendedor in self.vendedores:
            total = 0
            for venta in self.vendedores[vendedor]:
                total += venta

            if total > mayor_total:
                mayor_total = total
                mejor = vendedor

        if mejor is not None:
            print(f"El mejor vendedor es {mejor} con ventas totales de ${mayor_total}")
        else:
            print("No hay ventas registradas")


sistema = SistemaVentas()
sistema.agregar_vendedor("Jose")
sistema.agregar_vendedor("Armando")
sistema.agregar_vendedor("Juan")
sistema.registrar_venta("Jose", 350)
sistema.registrar_venta("Jose", 400)
sistema.registrar_venta("Armando", 600)
sistema.registrar_venta("Armando", 850)
sistema.registrar_venta("Juan", 500)

sistema.mostrar_ventas()
print("-----------------------")
sistema.total_vendedor("AnaJose")
sistema.total_vendedor("Armando")
sistema.total_vendedor("Juan")

sistema.mejor_vendedor()