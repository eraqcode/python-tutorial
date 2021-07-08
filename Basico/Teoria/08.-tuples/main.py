
numeros_enteros = (-20,-15, -4, -1, 0, 4, 18, 41)

for numero in numeros_enteros:
    print(numero)

# A tuple can not be change the values and also we can add more items
# if we wnat to add items we can transform the tuple in a list
# For example:

fruits = ("apple", "pear", "pinneaple", " orange")
fruists_list = list(fruits)
fruists_list[1] = "grape"

fruists_list.append("blackberry")

tuple_fruits = tuple(fruists_list)
print(tuple_fruits)
for fruit in tuple_fruits:
    print(fruit)