from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('Label')
root.geometry('780x580')

frame = Frame(root)
frame.pack(fill = 'both', expand = True)
frame.config(
    bg = '#00003b',
    borderwidth ='8',
    relief = 'ridge',
)

label = Label(frame, text = 'Hola Mundo')
label.grid(row = 0, column = 0, sticky = 'w')
label.config(
    font = ('Arial', 20),
    bg = '#00003b',
    fg = 'white',
    padx = '10'
)


#insertar una imagen en un label
label__imagen = Label(frame)
imagen = Image.open('C:/Users/Erik\Documents/Programacion/Programacion Python/GUI/3.-label/auto.jpg')
photo = ImageTk.PhotoImage(imagen)
label__imagen.grid(row = 2, column = 0)
label__imagen.config(image = photo, padx = '10', pady = '15' )

root.mainloop()