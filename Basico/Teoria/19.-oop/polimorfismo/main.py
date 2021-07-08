""" Polimorfismo """
class Manzana:
    
    def tipo(self):
        print("Fruta")

    def color(self):
        print("Roja")

class Zanahoria:
    def tipo(self):
        print("Vegetal")

    def color(self):
        print("Naranja")

class Papa:
    def tipo(self):
        print("Tuberculo")

    def color(self):
        print("Marron")

""" polimorfismo por funcion """
def acceso_polimorfismo(objeto):
    objeto.tipo()
    objeto.color()           

obj1 = Manzana()
obj2 = Zanahoria()
obj3 = Papa()

acceso_polimorfismo(obj3)