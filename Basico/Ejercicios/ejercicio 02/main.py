# Ejercicio para invertir numeros

numero = int( input("Numero: ") )
aux = 0

while numero > 0:
    aux = aux + numero % 10
    aux = aux * 10
    numero = numero // 10

print(aux // 10)