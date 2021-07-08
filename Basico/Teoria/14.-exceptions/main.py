
""" Manejo de errores """

try:
    dividendo = int( input("Ingrese el dividendo: ") )
    divisor = int( input("Ingrese el divisor: ") )
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    else:
        result = dividendo / divisor
   
except ValueError as err:
    print("El valor ingresado debe ser entero ", err)  
except ZeroDivisionError as err:
    print(err)
else:
    print("Todo ha salido bien asi que")
    print(f"aqui tienes tu resultado: {result: 0}")    
finally:
    print("Eso es todo Amigo/a")