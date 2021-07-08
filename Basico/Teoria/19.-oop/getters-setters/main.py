""" Getters y Setters """

class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__altura = 0

    #==========================
    #     METODOS DE ACCESO   =
    # =========================    

    #getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_altura(self):
        return self.__altura

    #setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_altura(self, altura):
        self.__altura = altura  

persona1 = Persona()   
persona1.set_nombre("Andres")
persona1.set_edad(24)
persona1.set_altura(174)

print(f"Hola soy {persona1.get_nombre()} tengo {persona1.get_edad()} y mido {persona1.get_altura()}")
        
    

