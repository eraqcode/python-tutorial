""" Serializacio con objetos """

import pickle

class Frutas:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def imprimir(self):
        print(f"Fruta: {self.__nombre}, Tipo: {self.__tipo}")

fruta1 = Frutas("Manzana", "Dulce")
fruta2 = Frutas("Naranja", "Citrico")
fruta3 = Frutas("Limon", "Citrico")
fruta4 = Frutas("Nuez", "Seca")

lista_frutas = [fruta1, fruta2, fruta3, fruta4]

with open("fruta", mode = "wb") as frutas_file:
    pickle.dump(lista_frutas, frutas_file)


with open("fruta", mode = "rb") as frutas_file:
    frutas = pickle.load(frutas_file)
    for fruta in frutas:
        print(fruta.imprimir())