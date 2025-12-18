# Gestión básica de calificaciones de un grupo
class Grupo:
    def __init__(self, Nombre_Grupo):
        self.Nombre_Grupo = Nombre_Grupo
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def mostrar_calificaciones(self):
        no_elementos = len(self.calificaciones)

        for elemento in range(no_elementos):
            print(f"{elemento + 1} {self.calificaciones[elemento]}")
    
    def obtener_calificacion(self, indice):
       print(f"Indice: {indice} calificacion {self.calificaciones[indice - 1]}")

gpo1 = Grupo("TICs 3A")
gpo1.agregar_calificacion(8)
gpo1.agregar_calificacion(10)
gpo1.agregar_calificacion(9)
gpo1.agregar_calificacion(10)
gpo1.agregar_calificacion(7)
gpo1.agregar_calificacion(6)
gpo1.agregar_calificacion(7)
indice = int(input("Dame el valor del indice"))
             
gpo1.obtener_calificacion(indice)
