import tkinter as tk

class ContCreciente(tk.Tk):
    def __init__(self):
        super().__init__()

        self.contador = 0
        self.resizable(False,False)
        self.configure(bg='navyblue')
        self.title("Contador")

        # Crear los componentes usando grid
        self.etiqueta = tk.Label(self, text="Contador")
        self.etiqueta.grid(row=0, column=0, padx=10, pady=10)  # Etiqueta en la primera fila, primera columna

        self.mostrador_contador = tk.Entry(self, state='readonly')
        self.mostrador_contador.grid(row=0, column=1, padx=10, pady=10)  # Campo de entrada en la primera fila, segunda columna

        self.boton = tk.Button(self, text="Count Up", command=self.incrementar_contador)
        self.boton.grid(row=0, column=2, padx=10, pady=10)  # Botón en la primera fila, segunda columna

        self.boton = tk.Button(self, text="Count Down", command=self.decreciente_contador)
        self.boton.grid(row=0, column=3, padx=10, pady=10)  # Botón en la primera fila, tercera columna

        self.boton = tk.Button(self, text="Reset", command=self.comienzo_contador)
        self.boton.grid(row=0, column=4, padx=10, pady=10)  # Botón en la primera fila, cuarta columna


        # Actualizar el mostrador del contador inmediatamente
        self.actualizar_mostrador_contador()

    def actualizar_mostrador_contador(self):
        self.mostrador_contador.config(state='normal')
        self.mostrador_contador.delete(0, tk.END)
        self.mostrador_contador.insert(0, str(self.contador))
        self.mostrador_contador.config(state='readonly')

    def incrementar_contador(self):
        self.contador += 1
        self.actualizar_mostrador_contador()
    def decreciente_contador(self):
        self.contador -= 1
        self.actualizar_mostrador_contador()
    def comienzo_contador(self):
        self.contador = 0
        self.actualizar_mostrador_contador()
    
# Crear la instancia de la clase ContCreciente y ejecutar la aplicación
ventana = ContCreciente()
ventana.mainloop()