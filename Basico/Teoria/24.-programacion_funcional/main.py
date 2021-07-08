import functools
import operator # modulo para realizar operaciones en listas

""" map() """

paises = ["Ecuador", "Argentina", "Francia", "Italia", "Uganda"]

def imprimir(pais):
    return pais

result = map(imprimir, paises)
print(list(result))

numeros = [2, 6, 3, 17, 14]
def sumar (n):
    return n + 4
result_numbers = map(sumar, numeros)
print(list(result_numbers))    

resultado3 = map( lambda x: x - 2, numeros )
print(f"Resultado 3: { list(resultado3) }")




""" filter """
def mayorque(n):
    return n > 10

result_filter = filter(mayorque, numeros)
print( "\t",list(result_filter) )



""" reduce() """
print("La suma total de la lista numeros es: ")
print( functools.reduce( lambda a, b: a + b, numeros ) )

print("La resta total de la lista numeros es: ")
print( functools.reduce( operator.sub, numeros ) )