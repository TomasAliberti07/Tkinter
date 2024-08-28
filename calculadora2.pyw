import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.configure(bg='black')
        self.operacion = tk.StringVar(value="sumar")

        # Etiquetas
        self.label1 = tk.Label(self, text="Primer número", bg='LightBlue')
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.label2 = tk.Label(self, text="Segundo número", bg='LightBlue')
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.label_resultado = tk.Label(self, text="Resultado", bg='LightBlue')
        self.label_resultado.grid(row=2, column=0, padx=10, pady=10)

        # Campos de entrada
        self.lineEdit1 = tk.Entry(self)
        self.lineEdit1.grid(row=0, column=1, padx=10, pady=10)

        self.lineEdit2 = tk.Entry(self)
        self.lineEdit2.grid(row=1, column=1, padx=10, pady=10)

        self.lineEdit_resultado = tk.Entry(self, state='readonly')
        self.lineEdit_resultado.grid(row=2, column=1, padx=10, pady=10)
        self.lineEdit_resultado.insert(0, "0")

        # Radiobuttons para seleccionar la operación
        tk.Radiobutton(self, text="+", variable=self.operacion, value="sumar", bg='LightBlue').grid(row=3, column=0, padx=10, pady=10)
        tk.Radiobutton(self, text="-", variable=self.operacion, value="restar", bg='LightBlue').grid(row=3, column=1, padx=10, pady=10)
        tk.Radiobutton(self, text="*", variable=self.operacion, value="multiplicar", bg='LightBlue').grid(row=4, column=0, padx=10, pady=10)
        tk.Radiobutton(self, text="/", variable=self.operacion, value="dividir", bg='LightBlue').grid(row=4, column=1, padx=10, pady=10)

        # Botón para calcular el resultado
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=5, columnspan=2, pady=10, sticky='nsew')

        # Botón para reiniciar
        tk.Button(self, text="RESET", command=self.reset).grid(row=6, columnspan=2, pady=10, sticky='nsew')

    def calcular(self):
        # Obtener los valores de los campos de entrada
        try:
            num1 = float(self.lineEdit1.get())
            num2 = float(self.lineEdit2.get())
        except ValueError:
            # Si hay un error en la conversión, mostrar "Error"
            self.lineEdit_resultado.config(state='normal')
            self.lineEdit_resultado.delete(0, tk.END)
            self.lineEdit_resultado.insert(0, "Error")
            self.lineEdit_resultado.config(state='readonly')
            return

        operacion = self.operacion.get()

        # Realizar la operación seleccionada
        if operacion == "sumar":
            resultado = num1 + num2
        elif operacion == "restar":
            resultado = num1 - num2
        elif operacion == "multiplicar":
            resultado = num1 * num2
        elif operacion == "dividir":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Div/0"  # Manejo simple de división por cero
        else:
            resultado = "Error"

        # Mostrar el resultado
        self.lineEdit_resultado.config(state='normal')
        self.lineEdit_resultado.delete(0, tk.END)
        self.lineEdit_resultado.insert(0, str(resultado))
        self.lineEdit_resultado.config(state='readonly')

    def reset(self):
        self.lineEdit1.delete(0, tk.END)
        self.lineEdit2.delete(0, tk.END)
        self.lineEdit_resultado.config(state='normal')
        self.lineEdit_resultado.delete(0, tk.END)
        self.lineEdit_resultado.insert(0, "0")
        self.lineEdit_resultado.config(state='readonly')

# Crear la instancia de la aplicación y ejecutar el bucle principal
ventana = Calculadora()
ventana.mainloop()
