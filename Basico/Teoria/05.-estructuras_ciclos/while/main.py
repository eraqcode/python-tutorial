# -*- coding: utf-8 -*-
# SUMA DE N NUMEROS

flag = True
suma = 0
print("Suma de n numeros")
while flag:
    numero = int( input("Ingrese un numero: ") )
    suma += numero
    if input("Desea ingresar otro numero (s/n)? ") == "n":
        flag = False
print(f'Suma Total = { suma } ')        