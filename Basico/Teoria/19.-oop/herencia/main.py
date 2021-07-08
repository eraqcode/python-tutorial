""" Herencia """
import os

#Clase Padre
class Persona:
    def __init__(self):
        self.__nombre = "Jose"
        self.__edad = 0
        self.__pais = ""
        self.__ciudad = ""

    def ingresar_datos(self):
        try:
            self._nombre = input("Ingresa tu nombre: ")
            self._edad = int( input("Ingresa tu edad: ") )
            self._pais = input("Ingresa tu pais: ")
            self._ciudad =input("Ingresa tu ciudad: ")
        except ValueError:
            print("Ha ingresado un valor incorrecto")

    def imprir_datos(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}") 
        print(f"Pais: {self._pais}")
        print(f"Ciudad: {self._ciudad}")



class Estudiante(Persona):
    def __init__(self):
        self.__codigo = ""
        self.carrera = ""

        """ Constructor clase padre """
        super().__init__()

    def add_data(self):
        self.__codigo = input("Ingresa tu codigo id: ")
        self.__carrera = input("Ingresa tu carrera: ")
        self.ingresar_datos()

    def print_data(self):
        print(f"Codigo: {self.__codigo}")
        print(f"Carrera: {self.__carrera}")      
        self.imprir_datos()  


estudiante1 = Estudiante()
estudiante1.add_data()
os.system("pause")
os.system("cls")
estudiante1.print_data()