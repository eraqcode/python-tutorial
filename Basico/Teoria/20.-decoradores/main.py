 #D ecorador - formado por 3 funciones
 # Cambia la funcionalidad de una funcion, clase o metodo
 # es un PATRON DE DISEÑO

from time import time
#algo mas dificil
def speed_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        finish_time = time()
        print(f"Tomo {finish_time - start_time} s")
    return wrapper

@speed_time
def long_time():
    for i in range(2400000):
        i*6


#algo mas facil y entendible

def decorador(func):
    #Funcion interior - agregando funcionalidad extra
    def wrapper(a, b):
        print("**********")
        print(f"   {func(a, b)}")
        print("**********\n")
    return wrapper

#Aplicando decorador
@decorador
def suma(a, b):
    return a + b

@decorador
def resta(a, b):
    return a - b

@decorador
def potencia(a, b):
    return a ** b

#Llamadas a las funciones
suma(18, 48)
resta(28, 147)
potencia(2, 7)
long_time()