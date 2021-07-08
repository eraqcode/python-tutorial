# Verificacion de numero palindromo
import os
os.system("color 1F")
print("\t\t\t\tBIENVENIDOS")
print("\n")
print("Este programa verificara si un numero ingresado es palindromo")
print("\n")
os.system("pause") # pausa en la consola
os.system("cls") # limpio la consola

os.system("color 0A") #cambio color de fondo y letra
numero = int( input("Ingrese el numero a verficar: ") )
numero_normal = numero
aux = 0 

# Invirtiendo el numero
while numero > 0:
    aux = aux + numero % 10
    aux = aux * 10
    numero //= 10
numero_invertido = aux // 10

# Verificando si es numero palindromo
if numero_normal == numero_invertido:
    print(f" {numero_normal} es palindromo ")
else:
    print(f" {numero_normal} no es palindromo ")   