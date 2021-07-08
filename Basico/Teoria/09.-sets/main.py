paises_mundo = {"Alemania", "España", "Ecuador", "Argentina", "Japon", "Nigeria", "italia", "Canada"}
paises_europa = {"Italia", "España", "Rusia", "Polonia", "Portugal"}

# imprimir elemento de un cnjunto
for paises in paises_mundo:
    print(paises)

#agregar elementos
paises_mundo.add("Polonia")
paises_mundo.update(["Egipto", "Brasil", "Australia"])

print("\n")
for paises in paises_mundo:
    print(paises)

#eliminacion de datos

paises_mundo.discard("Polonia")
paises_mundo.pop()
paises_mundo.remove("Nigeria")
print("\n")
for paises in paises_mundo:
    print(paises)

# Operaciones con conjuntos
# Union
paises = paises_mundo.union(paises_europa)    
print("\nPaises Unidos")
for pais in paises:
    print(pais)

#interseccion
paises_comunes = paises_mundo.intersection(paises_europa)
print("\nPaises comunes")
for paises in paises_comunes:
    print(paises)