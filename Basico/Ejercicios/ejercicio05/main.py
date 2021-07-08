""" Crear un progrmma que perita adivinar un numero
    aleatorio entre 0 y 100 al final se debera mostrar 
    el numero de intentos realizados por el usuario
"""
import random
def juego():
    try:
        random_number = random.randint(0, 11)
        flag = True
        cont = 0
        user_name = input("Enter your name: ")
        
        while flag:
            user_number = int( input("Enter a number") )
            if user_number < random_number:
                print("Your number is smaller")
            elif user_number > random_number:
                print("Your number is bigger")
            else:
                print(f"Great {user_name}!!!, You guessed in {cont} attempts")
                flag = False        
            cont += 1
    except ValueError:
         print("An error has ocurred")
    except TypeError as e:
         print(e)

juego()