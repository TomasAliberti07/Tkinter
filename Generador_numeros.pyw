import tkinter as tk
from tkinter import Spinbox
import random

class GeneradorNumeros(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de Números")
        self.configure(bg='lavender')
        # Etiquetas
        self.label_num1 = tk.Label(self, text="Número 1")
        self.label_num1.grid(row=0, column=0, padx=10, pady=10)

        self.label_num2 = tk.Label(self, text="Número 2")
        self.label_num2.grid(row=1, column=0, padx=10, pady=10)

        self.label_generado = tk.Label(self, text="Número Generado")
        self.label_generado.grid(row=2, column=0, padx=10, pady=10)

        # Spinbox para el primer número
        self.spinbox_num1 = Spinbox(self, from_=0, to=100)
        self.spinbox_num1.grid(row=0, column=1, padx=10, pady=10)

        # Spinbox para el segundo número
        self.spinbox_num2 = Spinbox(self, from_=0, to=100)
        self.spinbox_num2.grid(row=1, column=1, padx=10, pady=10)

        # Campo de entrada para mostrar el número generado (no editable)
        self.entry_generado = tk.Entry(self, state='readonly')
        self.entry_generado.grid(row=2, column=1, padx=10, pady=10)

        # Botón "Generar"
        self.button_generar = tk.Button(self, text="Generar", command=self.generar_numero)
        self.button_generar.grid(row=3, columnspan=2, pady=10)

    def generar_numero(self):
        # Obtener valores de los Spinboxes
        num1 = int(self.spinbox_num1.get())
        num2 = int(self.spinbox_num2.get())
        
        # Asegurarse de que el primer número sea menor o igual que el segundo
        if num1 > num2:
            num1, num2 = num2, num1

        # Generar un número aleatorio en el rango especificado
        numero_generado = random.randint(num1, num2)
        
        # Mostrar el número generado en el campo de entrada
        self.entry_generado.config(state='normal')
        self.entry_generado.delete(0, tk.END)
        self.entry_generado.insert(0, str(numero_generado))
        self.entry_generado.config(state='readonly')

# Crear la instancia de la aplicación y ejecutar el bucle principal
ventana = GeneradorNumeros()
ventana.mainloop()
