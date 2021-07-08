import math

def esphere_volumen(radio):
    volumen = (4 / 3) * (math.pi * radio ** 3)
    return volumen

def cylinder_valumen(radio, height):
    volumen = radio **2 * math.pi * height
    return volumen

