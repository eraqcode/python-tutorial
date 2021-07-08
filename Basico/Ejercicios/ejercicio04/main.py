"""
    Se necesita crear un programa para un consecionario de autos, el progrma
    consite en permitir ingresar marcas de autos por pais, es decir el usuario
    ingresara un pais seguido de una lista de marcas de autos.
    El programa debera consultar con el usuario si desea ingresar mas autos
    si la respuesta es no, debera preguntar si desea ingresr otro pais
"""
 
def cars():
    flag = True
    
    brands_car = {}
    
    while flag:
        flag_brands = True
        name_country = input("Enter the name of the country: ")
        brands_car[name_country] = []
        while flag_brands:
            name_brand_car = input("Enter the name of the brand: ")
            brands_car[name_country].append(name_brand_car)
            if input("Do you want to enter other brand (y/n)? ") == "n":
                flag_brands = False
        if input("Do you want to enter other country (y/n)? ") == "n":
                flag = False        
    return brands_car

def print_cars():
    car = cars()
    for country, brand in car.items():
        print(f"{country} :")
        for b in brand:
            print(f"\t{b}")
print_cars()
