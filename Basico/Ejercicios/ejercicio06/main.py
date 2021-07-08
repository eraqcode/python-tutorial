"""
    Crear un clase de nombre librola cual permitira al usuario
    ingresar una cantidad de libros con su nombre, autor, editorial
    y año de publicacion
"""
class Libros:
    
    def __init__(self):
        self.libro = {}
    def addData(self):
        insert = True
        while insert:
            nombre = input("Ingrese el nombre del libro: ")
            autor = input("Ingrese el autor: ")
            editorial = input("Ingrese la editorial: ")
            anyo_publicacion = input("Ingrese año de publicacion: ")
            lib_atributos = {'Autor': autor, 'Editorial': editorial, 'Año de Publicacion': anyo_publicacion}
            self.libro[nombre] = lib_atributos
            print()
            if input('Desea ingresar otro libro (s/n)? ') == 'n':
                insert = False

    def showData(self):
        for nombre, valor in self.libro.items():
            autor = valor['Autor']   
            editorial = valor['Editorial']
            anyo = valor['Año de Publicacion']
            print(f"Nombre: {nombre}\nAutor: {autor}\nEditorial: {editorial}\nAño de Publicacion: {anyo}")
            print()
            print("=========================================") 
            print()        
    
libro = Libros()
libro.addData()
libro.showData()