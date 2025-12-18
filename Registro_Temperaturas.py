class RegistroTemperaturas:
    def __init__(self):
        self.temperaturas = []

    def agregar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def mostrar_temperaturas(self):
        no_elementos = len(self.temperaturas)
        
        for elemento in range(no_elementos):
            print(f"{elemento + 1} {self.temperaturas[elemento]}")

    def contar_mayores_a(self, valor):
        temp_mayores = 0

        for temp in self.temperaturas:
            if temp > valor:
                temp_mayores += 1

        return temp_mayores


registro = RegistroTemperaturas()

registro.agregar_temperatura(5)
registro.agregar_temperatura(7)
registro.agregar_temperatura(12)
registro.agregar_temperatura(14)
registro.mostrar_temperaturas()
print(registro.contar_mayores_a(1))

