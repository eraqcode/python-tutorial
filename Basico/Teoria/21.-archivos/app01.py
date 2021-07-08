from io import open

with open('deportes.txt', mode= 'w') as my_file:
    my_file.write("Futbol\nBasket\nTenis\nFutbol Americado")


with open('deportes.txt', mode= 'r') as file:
    data = file.readlines()
    for line in data:
        print(line)
