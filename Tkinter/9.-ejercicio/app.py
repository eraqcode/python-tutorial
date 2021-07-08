from tkinter import *

root = Tk()
varOpcion = IntVar()
ficha_usuario = ''
def get_opcion():
    global ficha_usuario
    if varOpcion.get() == 1:
        ficha_usuario = 'X'
    else:
        ficha_usuario = 'O'   

def click():
    button.config(text = ficha_usuario)
    print( button['text'] )

root.title('Ejercicio')
frame = Frame(root)
frame.pack()

ficha_x = Radiobutton(frame, text = 'X', value = 1, variable = varOpcion, command = get_opcion)
ficha_x.grid(row = 1, column = 1, sticky = 'w')
ficha_x = Radiobutton(frame, text = 'O', value = 2, variable = varOpcion, command = get_opcion)
ficha_x.grid(row = 2, column = 1, sticky = 'w')

button = Button(frame, text = '', command = click)
button.grid(row = 3, column = 1)
root.mainloop()