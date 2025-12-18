# Gestión básica de una lista de reproducción
class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    # Metodo
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    # Metodo
    def mostrar_canciones(self):
        elementos = len(self.canciones)
        for elemento in range(elementos):
            print(f"{elemento +1} {self.canciones [elemento]}")
    

lista = ListaReproduccion("Rock")
print("-------------------------------------")

lista.agregar_cancion("La carta-Heroes del Silencio")
lista.agregar_cancion("Entre Tus Jardines-Jaguares")
lista.agregar_cancion("Yo Quiero Ser-Perro Callejero")

lista.mostrar_canciones()
print("-------------------------------------")

