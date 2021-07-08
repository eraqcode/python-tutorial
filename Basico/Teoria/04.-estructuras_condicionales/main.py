# -*- coding: utf-8 -*-
#Condicionales if, if-else, if elif else

edad = int( input('Ingresa tu edad: ') )
if edad < 18:
    print("Tu eres menor de edad")
else:
    print("Tu eres mayor de edad")    
    
nota_alumno = int( input("Ingresa la nota del alumno -> ") )
if nota_alumno < 13:
    print("No pasa el año")
elif nota_alumno >= 13 and nota_alumno <= 15:
    print("Te quedaste a supletorios")
else:
    print("Pasaste de año")         