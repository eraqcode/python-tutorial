from tkinter import * 
root = Tk()

root.title('Entry')
root.geometry('780x580')

frame = Frame(root)
frame.pack(fill = 'both', expand = True)
frame.config(bg = '#00003b')

titulo__label = Label(frame, text = 'Informacion Personal')
titulo__label.grid(row = 0, column = 6, sticky = 'n')
titulo__label.config(bg = '#00003b', fg = 'white', font = ('Arial', 15), relief = 'ridge')

nombre__label = Label(frame, text = 'Nombre')
nombre__label.grid(row = 1, column = 0, sticky = 'w')
nombre__label.config(bg = '#00003b', fg = 'white', font = ('Arial', 15), padx = '15', pady = '15')

apellido__label = Label(frame, text = 'Apellido')
apellido__label.grid(row = 2, column = 0, sticky = 'w')
apellido__label.config(bg = '#00003b', fg = 'white', font = ('Arial', 15), padx = '15', pady = '15')

password__label = Label(frame, text = 'Contraseña')
password__label.grid(row = 3, column = 0, sticky = 'w')
password__label.config(bg = '#00003b', fg = 'white', font = ('Arial', 15), padx = '15', pady = '15')

comentario__label = Label(frame, text = 'Comentario')
comentario__label.grid(row = 4, column = 0, sticky = 'w')
comentario__label.config(bg = '#00003b', fg = 'white', font = ('Arial', 15), padx = '15', pady = '15')


#Variable para el boton
mi__nombre = StringVar()
#creacion del entry
nombre__entry = Entry(frame, textvariable = mi__nombre)
nombre__entry.grid(row = 1, column = 1)
apellido__entry = Entry(frame)
apellido__entry.grid(row = 2, column = 1)
password__entry = Entry(frame)
password__entry.grid(row = 3, column = 1)
password__entry.config(show = '■')

#Creacion de textarea
comentario = Text(frame, width = 22, height = 8)
comentario.grid(row = 4, column = 1,  padx = '15', pady = '15')

#Creacion de un scrollvar
scroll__vertical = Scrollbar(frame, command = comentario.yview)
scroll__vertical.grid(row = 4, column = 2, sticky = 'nsew')
comentario.config(bg = 'lightgray', fg = 'darkblue', font = ('Bauhaus 93 Normal', 14), yscrollcommand = scroll__vertical.set)

#Creacion de botones
def btn__accion():
    mi__nombre.set('Erik Andres')

btn__enviar = Button(frame, text = 'Enviar', width = 10, command = btn__accion)
btn__enviar.grid(row = 6, column = 1)
btn__enviar.config(bg = 'lightblue')
root.mainloop()