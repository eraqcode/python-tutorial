# String Methods

text = 'Quito es la capital del Ecuador'

#len() - tamaño de la cadena
print(f"{len(text)}")

# slicing - extraer parte del string
print(f"{ text[-15 : -5] }")

#strip() - quita los espacios en blanco si es que lo hay

#lower() - transforma la cadena a minusculas
print(f"{text.lower()}")

#upper() - transforma la cadena a mayusculas
print(f"{text.upper()}")

#replace() - reemplaza una cadena o caracter por otro
print(f'{text.replace("Ecuador", "Pichincha")}')

#Verificar si una sub cadena esta dentro del string
print("Quito" in text)

#count() - cuenta el numero de caracteres o strings en la cadena
print(f"{text.count('es')}")

#finc() - retorna la posicion de una sub cadena
print(f"{text.find('capital')}")
