""" Serializacion """

import pickle

aerolineas_list = ['LATAM', 'Air Canada', 'Lufthansa', 'Iberia', 'GOL','Air Mexico']

with open("aerolineas", mode = "wb") as file:
    pickle.dump(aerolineas_list, file)

with open("aerolineas", mode = "rb") as file:
    aerolineas = pickle.load(file)    
    for aerolinea in aerolineas:
        print(aerolinea)