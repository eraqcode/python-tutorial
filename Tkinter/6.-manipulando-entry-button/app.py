from tkinter import *

class Ejercicio:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Ejercicio')
        self.ventana.config(bg = '#00003b')
       
        #Frame
        self.frame = Frame(self.ventana)
        self.frame.pack(fill = 'both', expand = True)
        self.frame.config(bg = '#00003b')

        #pantalla
        self.pantalla = Entry(self.frame)
        self.pantalla.grid(row = 0, column = 0, columnspan = 2, padx = 15, pady = 15)
        self.pantalla.config(width = 48)

        self.resultado = Entry(self.frame)
        self.resultado.grid(row = 1, column = 0, columnspan = 2, padx = 15, pady = 15)
        self.resultado.config(width = 48, bg = 'black', fg = 'lightgreen', font = ('Heltica', 18), relief = 'ridge')
        #indice
        self.i = 0

        #Imprimir numero del boton en pantalla
        
        #botones
        self.boton1 = Button(self.frame, text = 2, width = 10, height = 2, font = ('Heltica', 18), command = lambda: self.click_boton("2"))
        self.boton1.grid(row = 2, column = 0, columnspan = 1)
        
        self.boton2 = Button(self.frame, text = 22, width = 10, height = 2, font = ('Heltica', 18),command = lambda: self.click_boton("22")) 
        self.boton2.grid(row = 2, column = 1, columnspan = 1)
        
        self.boton_sumar = Button(self.frame, text = '+', width = 10, height = 2, font = ('Heltica', 18),command = lambda: self.click_boton("+"))
        self.boton_sumar.grid(row = 3, column = 0, columnspan = 1)
        
        self.boton_igual = Button(self.frame, text = '=', width = 10, height = 2, font = ('Heltica', 18), command = self.ecuacion)
        self.boton_igual.grid(row = 3, column = 1, columnspan = 1)
    
    def click_boton(self, texto):
           self.pantalla.insert(self.i, texto)
           self.i += 1

    def ecuacion(self):
        result = self.pantalla.get()   
        total = eval( result )
        print(total)
        self.resultado.insert(0, total)
        self.i += 1 
root = Tk()
ejercicio = Ejercicio(root)
root.mainloop()