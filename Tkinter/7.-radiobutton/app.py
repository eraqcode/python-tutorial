from tkinter import *

root = Tk()

var_opcion = IntVar() # esta variable es necesaria permite el control del valor del radiobutton

def imprimir():
    if var_opcion.get() == 1:
        descripcion.config(text = 'Has escojigo la opcion masculino',  bg = 'darkgreen', font = ('Arial', 18), fg = 'white')
    else:
        descripcion.config(text = 'Has escojigo la opcion femenino',  bg = 'darkgreen', font = ('Arial', 18), fg = 'white')
    

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

radio_masculino = Radiobutton(frame, text = 'Masculino', variable = var_opcion, value = 1, command = imprimir)
radio_masculino.grid(row = 1, column = 2)
radio_masculino.config(bg='darkgreen', fg = 'white')
radio_femenino = Radiobutton(frame, text = 'Femenino', variable = var_opcion, value = 2, command = imprimir)
radio_femenino.config(bg='darkgreen', fg = 'white')
radio_femenino.grid(row = 2, column = 2)



root.mainloop()