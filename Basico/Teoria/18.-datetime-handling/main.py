# date and time handling
"""
    paquete datetime
    -datetime
    -time
    -date
"""
from datetime import datetime

"""fecha = date.today()
print(f"Hoy es {fecha.day} / {fecha.month} / {fecha.year}")
"""

#Crear un objeto datetime
# datetime(year, month, day, hour, minutes                                                                                , seconds)
fecha = datetime(2020, 5, 9, 12, 55, 5)
print(fecha)

""" imprimir fecha y hora actual """

fecha_actual = datetime.now()
print(f"{ fecha_actual.year }/{ fecha_actual.month }/{ fecha_actual.day } ")
print(f"{ fecha_actual.hour } : { fecha_actual.minute } : { fecha_actual.second } ")

"""  Formato a fechas """
new_date = datetime.now()
print(new_date.strftime("%d/%B/%Y"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         