# Use of **kargs or key arguments in python
def capitals(**countries):
    for country, capital in countries.items():
        print(f'{country} : {capital}')

capitals(Alemania = 'Berlin', Austria = 'Viena', Francia = 'Paris')