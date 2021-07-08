import random

#creando un numero aleatorio dentro de un rango
print( random.randrange(1, 11) )
print( random.randint(15, 35) )

#tomar un elemento aleatorio de una lista
animales = ["tigre", "leon", "elefante", "perro", "gato"]
print( random.choice(animales) )