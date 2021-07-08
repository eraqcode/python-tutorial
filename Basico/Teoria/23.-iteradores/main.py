tupla = ("facebook", "instagram", "twitter", "hangouts")

my_iterador = iter(tupla)

print(next(my_iterador))

""" Creacion de un iterador """
class Iterador:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # permite detener la iteracion
incremento = Iterador()
myiter = iter(incremento)

print(next(myiter))
print(next(myiter))


""" Generador """
def incrementar(limite):
    numero = 0
    while numero < limite:
        yield numero
        numero += 1



generador = incrementar(10)
print()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
