""" Metodosde acceso - Forma Correcta """

class Persona:
    def __init__(self):
        self._nombre = "Jorge"
        self._edad = 0
        self._altura = 0

    #==========================
    #     METODOS DE ACCESO   =
    # =========================    

    """ getters """
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(edad):
        return self._edad

    @property
    def altura(self):
        return self._altura

    """ Setters """
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @altura.setter
    def altura(self, altura):
        self._altura = altura     

       

persona1 = Persona()

persona1.nombre = "Pepito Granada"
persona1.edad = 38
persona1.altura = 198

print(persona1.nombre)