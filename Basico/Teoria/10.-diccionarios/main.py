
paises_capitales = {"Alemania": "Berlin",
                    "Argentina": "Buenos Aires",
                    "Corea del Sur": "Seul",
                    "Libano": "Beirut"}

#imprimir un diccionario
for i in paises_capitales.keys():
    print(i)            

print("\n")
for i in paises_capitales.values():
    print(i)

print("\n")
for pais, capital in paises_capitales.items():
    print( f"{pais} : {capital}" )


#agregar datos a un diccionario
paises_capitales["Grecia"] = "Atenas"
paises_capitales.update({"Australia": "Camberra", "Arabia Saudi": "Rihad"})
print("\n")
for pais, capital in paises_capitales.items():
    print( f"{pais} : {capital}" )


#eliminar datos del diccionario
paises_capitales.pop("Grecia")    
print("\n")
for pais, capital in paises_capitales.items():
    print( f"{pais} : {capital}" )


#Diccionarios y listas
lenguajes_programacion = {"Compilados": ["C++", "C#", "Go", "Rust"],
                          "Interpretados": {"Python", "Javascript", "PHP"} 
                         }
print("\n")                         
for i, j in lenguajes_programacion.items():
    print(f"{i}:") 
    for k in j:
        print(f"\t-{k}")          

            