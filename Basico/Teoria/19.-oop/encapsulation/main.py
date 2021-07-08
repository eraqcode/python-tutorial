class Car:
    def __init__(self):
       # Private Variables
       self.__max_speed = 320
       self.__brand = 'Suzuki'
        
        
    def drive(self):
        print('driving')

    #private method
    # a private methos is not accessible from the object
    def __updateSoftware(self):
        print('Updating Software')

blue_car = Car()
blue_car.drive()

""" how can we access to a private method """
#object.-class_name__name_method

blue_car._Car__updateSoftware()


# private variables
red_car = Car()

""" accessing to a private variable """
# object.-class_name.__variable_name
print(f'Car Max Speed: { red_car._Car__max_speed }km/h ' )
print(f'Car Brand: { red_car._Car__brand } ' )