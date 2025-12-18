#Registro Alumnos

class RegistroAlumnos:
    def __init__(self):
        self.alumnos = {}
    
    def agregar_alumno(self, nombre):
        self.alumnos[nombre] = []
    
    def agregar_calificacion(self, nombre, cal):
        # Si el alumno existe agregar calificacion
        if nombre in self.alumnos:
            self.alumnos[nombre].append(cal)
        else:
            print("{nombre} no existe!")

    def mostrar_registro(self):
        for alumno in self.alumnos:
            print(f"{alumno} :{self.alumnos[alumno]}")
        
    def promedio_alumno(self, nombre):
        if nombre in self.alumnos:
            calificaciones = self.alumnos[nombre]
            promedio = sum(calificaciones)/(len(calificaciones))
            print(f"{nombre}, promedio: {promedio} - {calificaciones}")
        else:
            print(f"{nombre} no exite!")

TICS_3A = RegistroAlumnos()
TICS_3A.agregar_alumno("Juan")
TICS_3A.agregar_alumno("Ana")
TICS_3A.agregar_calificacion("Juan", 8)
TICS_3A.agregar_calificacion("Juan", 9)
TICS_3A.agregar_calificacion("Juan", 10)
TICS_3A.agregar_calificacion("ANA", 5)
TICS_3A.agregar_calificacion("Ana", 10)
TICS_3A.agregar_calificacion("Ana", 5)
TICS_3A.agregar_calificacion("Ana", 5)
TICS_3A.mostrar_registro()
TICS_3A.promedio_alumno("Juan")
TICS_3A.promedio_alumno("Ana")