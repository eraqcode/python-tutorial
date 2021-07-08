""" Manejo de Archivos """
from io import open

file = open("frutas.txt", "wt")

file.write("Manzana\nPera\nUvas")

file.close()

# leer un archivo
file = open("frutas.txt", "rt")
print(file.read())
file.close()

file = open("frutas.txt", "at")
file.write("Naranja\nPera")
file.close()

#leer por linea
file = open("frutas.txt", "rt")
frutas = file.readlines()
file.close()
print( frutas[2] )
