"""
    Una empresa x necesita calcular el valor total de una factura, para lo cual ha 
    encargado al departamento de sistemas que desarrolle un programa opara que sus cajeros
    puedan ingresar el precio de cada producto, el dinero entregado por el cliente 
    e imprima en pantalla el valor toal de la factura, el dinero entregado por el cliente,
    el valor del cambio que se le debe dar al cliente, el subtotal y el total .
    
"""
import os

def supermercado():
    print("\n\n\n\n\t\t\t\Supermercado CODEX")
    print("\n\n\t\t\tSistema de Cobro")

def dinero_cliente():
    dinero = float( input("Monto entregado por el cliente: ") )

    return dinero

def valor_total():
    precios = []
    contador_productos = 1
    suma_total = 0
    
    numero_productos = int( input("Cuantos productos va a ingresar? -> ") )

    while numero_productos > 0:
        precio = float( input(f"Precio del producto #{contador_productos}: ") )
        precios.append( precio )
        suma_total = suma_total + precio

        #Contadores
        numero_productos = numero_productos - 1
        contador_productos += 1
    print("Lista de Precios: ")
    for precio in precios:
        print(f"\t\t{precio}")

    print(f"SUBTOTAL \t\t{suma_total}")
    print(f"\nTOTAL\t\t{ suma_total * 1.12 }")  

    dinero_cli = dinero_cliente()
    print(f"\n\n\nDinero Entregado: {dinero_cli}")
    if dinero_cli < suma_total:
        print(f"Cambio a Entregar: {suma_total*1.12 - dinero_cli}")
    else:
        print(f"Cambio a Entregar: {dinero_cli - suma_total * 1.12}")    

#impresion ppor pantalla
supermercado()
os.system("pause")
os.system("cls")

valor_total()