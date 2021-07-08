""" List Comprehension """
#Sintaxis: [expresion for item in lista]

"""h_letters = []
for letter in "humano":
    h_letters.append(letter)
   
print(h_letters)   
"""

h_letters = [letter for letter in "humano"]
print(h_letters)

number_list = [x * 3 for x in range(20) if x % 2 == 0]
for number in number_list:
    print(number)






""" Comprension de Diccionarios """

diccionario = {str(i): i for i in range(10)}
print(diccionario)

frutas = ["manzana", "naranja", "maracuya", "cereza"]
dict_frutas = {f: len(f) for f in frutas}
print(dict_frutas)


# enumerate devuelve la posicion de cada elemento
dict_enumerate = {f:i for i, f in enumerate(frutas)}
print(dict_enumerate)