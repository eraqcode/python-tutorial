"""
    numbers = [1, 2, 3, 4, 9]
    list = [x*2 for x in numbers]
    print(list)

"""

def pares(maximo):
    contador = 0
    while contador < maximo:
        yield contador ** 2
        contador += 1

generator = pares(10)

"""
print(f"\t{next(generator)}")
print(f"\t{next(generator)}")
print(f"\t{next(generator)}")
print(f"\t{next(generator)}")
"""
for numbers in generator:
    print(f"\t{numbers}")

#expression generator
list_numbers = [1, 2, 3, 4, 5]
generador = (x **2 for x in list_numbers)
print(next(generador))