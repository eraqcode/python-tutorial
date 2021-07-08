""" archivos02 """
from io import open
import os

file = open("frase.txt", "wt")
file.write("La rosa es blanca")
file.close()

#metodo writlines
file = open("frase.txt", "r+")
lista_frases = ["Esto es eso\n", "El chaleco de Simon Bolivar\n", "No tiene mangas de ningun color"]
file.writelines(lista_frases)
file.close()

file = open("frase.txt", "r")
print(file.read())
file.close()

#eliminar archivo

if os.path.exists("frase.txt"):
    os.remove("frase.txt")
else:
    print("El no se puede eliminar, no existe")    
