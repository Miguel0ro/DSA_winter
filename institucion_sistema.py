# Una institución desea representar personas dentro de un sistema sencillo
class Persona:
    # Constructor 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self. edad = edad

    # Metodo
    def saludar(self):
        print(f"Hola, soy{self.nombre} y tengo {self.edad} años")

     # Metodo
    def es_mayor_de_edad(self):
        return self.edad >= 18

persona1 = Persona("Juan Lopez", 28)
persona2 = Persona("Luis Rivas", 15)

persona1.saludar()
persona2.saludar()

print(persona1.es_mayor_de_edad()) # True
print(persona2.es_mayor_de_edad()) # False