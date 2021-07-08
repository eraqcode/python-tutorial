
#labmdas

suma = lambda numero_1, numero_2: numero_1 + numero_2

numero1 = int(input("Ingrese el primer numero a sumar: "))
numero2 = int(input("Ingrese el segundo numero a sumar: "))

print( suma(numero1, numero2) )

#anonymous functions lambdas
def add_more(number):
    return lambda x: x * number

#call the function
double = add_more(11)
print( double(2) )