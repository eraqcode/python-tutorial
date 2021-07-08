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

#creacion del entry
nombre__entry = Entry(frame)
nombre__entry.grid(row = 1, column = 1)
apellido__entry = Entry(frame)
apellido__entry.grid(row = 2, column = 1)
password__entry = Entry(frame)
password__entry.grid(row = 3, column = 1)
password__entry.config(show = '■')
root.mainloop()