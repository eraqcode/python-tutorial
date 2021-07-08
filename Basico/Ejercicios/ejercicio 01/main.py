
# Ha llegado la hora del pago alos empleados de EraqCode  Corporation
# para lo cual se debe realizar la impresion de los cheques, pero
# tenemos un problema y es que la tecla del numero 4 de nuestra maquina de
# cheques se ha roto, hemos optado por una solucion y es que  les daremos a 
#nuestros colaboradores dos chques, pero necesitamos crear un program para que nos diga las dos cantidades
# al sumarlas nos den el valor del sueldo de cada trabajador, dentro de 
#estas cantidades no puede haber el numero 0
total = input("Ingrese el precio total")
a = '0'
for i in range( len(total) ):
    if total[i] == '4':
        a += '1'
    else:
        a += '0'

b = int(a) - int(total)

print(f" { int(a) } + {b} = { int(total) } ")