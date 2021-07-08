# lists

frutas_citricas = ["naranja", "limon", "lima"]
frutas_dulces = ["manzana", "pera", "uva"]

#add items in the list
frutas_citricas.append("mandarina")
frutas_citricas.insert(1, "maracuya")

# print a list
print(frutas_citricas)
for fruta in frutas_citricas:
    print(fruta)

# remove items from a list
frutas_citricas.remove("limon")
frutas_citricas.pop()
print()
for fruta in frutas_citricas:
    print(fruta)

#change a item
frutas_citricas[0] = "uvilla"
print()
for fruta in frutas_citricas:
    print(fruta)

#copy a list
frutas = frutas_dulces.copy()
print()
for fruta in frutas:
    print(fruta)

# join two list
frutas_citricas.extend(frutas_dulces)
print()
for fruta in frutas_citricas:
    print(fruta)
   
#sort a list
frutas_citricas.sort()
print()
for fruta in frutas_citricas:
    print(fruta)   