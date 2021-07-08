# Creacion de Menus

from tkinter import *

root = Tk()

root.title('Menus con Tkinter')
root.geometry('780x580') 

frame = Frame(root)
frame.pack()

#BArra de Munes
barra_menu = Menu(root) # el menu siempre va anclado a la ventana no al frame
root.config(menu = barra_menu)
opcion_archivo = Menu(barra_menu, tearoff = 0)
opcion_edicion = Menu(barra_menu, tearoff = 0)
opcion_herramientas = Menu(barra_menu, tearoff = 0)
opcion_ayuda = Menu(barra_menu, tearoff = 0)

#Submenu de archivo
opcion_archivo.add_command(label = 'Archivo Nuevo')
opcion_archivo.add_command(label = 'Abrir Carpeta')
opcion_archivo.add_command(label = 'Guardar')
opcion_archivo.add_command(label = 'Guardar Como')
opcion_archivo.add_separator() #Creacion de un separador
opcion_archivo.add_command(label = 'Salir')

#submenu de edicion
opcion_edicion.add_command(label = 'Copiar')
opcion_edicion.add_command(label = 'Cortar')
opcion_edicion.add_command(label = 'Pegar')
opcion_edicion.add_command(label = 'Buscar')
opcion_edicion.add_command(label = 'Reemplazar')
opcion_edicion.add_command(label = 'Buscar y Reemplazar')

#Submenu de herramientas
opcion_herramientas.add_command(label = 'Terminal')
opcion_herramientas.add_command(label = 'Depurador')
opcion_herramientas.add_command(label = 'Ejecutar')
opcion_herramientas.add_command(label = 'Preferencias')

#Submenu de ayuda
opcion_ayuda.add_command(label = 'Bienvenido')
opcion_ayuda.add_command(label = 'Documentacion')
opcion_ayuda.add_command(label = 'Licencia')
opcion_ayuda.add_command(label = 'Tips y Trucos')
opcion_ayuda.add_command(label = 'Acerca De')

barra_menu.add_cascade(label = 'Archivo', menu = opcion_archivo)
barra_menu.add_cascade(label = 'Edicion', menu = opcion_edicion)
barra_menu.add_cascade(label = 'Herramientas', menu = opcion_herramientas)
barra_menu.add_cascade(label = 'Ayuda', menu = opcion_ayuda)



root.mainloop()