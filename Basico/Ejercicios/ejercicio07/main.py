
from googletrans import Translator
translator = Translator()

try:
    with open('deportes.txt', mode='r') as file:
        text = file.readlines()
        for line in text:
            translation = translator.translate(line, dest= 'en')
            print(translation)
except FileNotFoundError as e:
    print("Ha ocurrido un error con el archivo ", e)            