from tkinter import *
from tkinter import filedialog

root = Tk()

def abrir_archivo():
    file = filedialog.askopenfilename( initialdir = "C:/Users/Erik/Documents", title = 'Abrir',
    filetypes = [('Excel', ".xls"), ('Texto', '.txt')]
    )
    print(file)
def leer_archivo():
    file = filedialog.askopenfile(mode = 'r', filetypes = [('Archivos de Python', ".py")])
    print(file.read())


boton_abrir = Button(root, text = 'Abrir', command = abrir_archivo)
boton_abrir.grid(row = 0, column = 0)
boton_leer = Button(root, text = 'Leer archivo', command = leer_archivo)
boton_leer.grid(row = 0, column = 2)
root.mainloop()