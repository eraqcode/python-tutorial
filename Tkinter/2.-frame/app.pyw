# Frame

from tkinter import *
root = Tk()

root.title('Frame')
root.geometry('650x450')
#creacion de frame
frame = Frame(root)
#frame.pack(side = 'top', anchor = 'e')
frame.pack(fill = 'both', expand = True)
#frame.place(x = 100, y = 50)
frame.config(
    width = '250',
    height = '250',
    background = '#00003b'
)

root.mainloop()