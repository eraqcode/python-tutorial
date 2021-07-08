import doctest

def area_triangulo(base, altura):
    """
    Calcula el area de un triangulo

    >>> area_triangulo(3, 6)
    9.0

    >>> area_triangulo(4, 5)
    10.0
    """
    return (base*altura)/2


doctest.testmod()    
