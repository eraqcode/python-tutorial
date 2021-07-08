from tkinter import *
root = Tk()


futbol = IntVar() # esta variable es necesaria permite el control del valor del radiobutton
natacion = IntVar()
guitarra = IntVar()
cocinar = IntVar()
series = IntVar()

def imprimir():
    opcion = ''
    if(futbol.get() == 1):
        opcion += ' futbol'    
    if(natacion.get() == 1):
        opcion += ' natacion'
    if(guitarra.get() == 1):
        opcion += ' guitarra'
    if(cocinar.get() == 1):
        opcion += ' cocinar'
    if(series.get() == 1):
        opcion += ' series'  

    descripcion.config(text = opcion)         
root.title('Uso de Radio Buttons')
root.geometry('780x480')

frame = Frame(root)
frame.pack(fill = 'both', expand = True)
frame.config(bg = 'darkgreen')

titulo_label = Label(frame,text = 'Escoja su Genero')
titulo_label.grid(row = 0, column = 0, sticky = 'w', padx = 20, pady = 20)
titulo_label.config(bg = 'darkgreen', font = ('Helvetica', 16), fg = 'white')
descripcion = Label(frame, text = '')
descripcion.grid(row = 6, column = 1, columnspan = 5)

Checkbutton(frame, text = 'Futbol', bg = 'darkgreen', fg = 'white', variable = futbol, onvalue = 1, offvalue = 0, command = imprimir).grid(row = 1, column = 1, sticky = 'w')
Checkbutton(frame, text = 'Natacion', bg = 'darkgreen', fg = 'white', variable = natacion, onvalue = 1, offvalue = 0, command = imprimir).grid(row = 2, column = 1, sticky = 'w')
Checkbutton(frame, text = 'Tocar guitarra', bg = 'darkgreen', fg = 'white', variable = guitarra, onvalue = 1, offvalue = 0, command = imprimir).grid(row = 3, column = 1, sticky = 'w')
Checkbutton(frame, text = 'Cocinar', bg = 'darkgreen', fg = 'white', variable = cocinar, onvalue = 1, offvalue = 0, command = imprimir).grid(row = 4, column = 1, sticky = 'w')
Checkbutton(frame, text = 'Ver Series', bg = 'darkgreen', fg = 'white', variable = series, onvalue = 1, offvalue = 0, command = imprimir).grid(row = 5, column = 1, sticky = 'w')


root.mainloop()