import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.configure(bg='LightBlue')
        # Etiquetas
        self.label1 = tk.Label(self, text="Primer número")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.label2 = tk.Label(self, text="Segundo número")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.label_resultado = tk.Label(self, text="Resultado")
        self.label_resultado.grid(row=2, column=0, padx=10, pady=10)

        # Campos de entrada
        self.lineEdit1 = tk.Entry(self)
        self.lineEdit1.grid(row=0, column=1, padx=10, pady=10)

        self.lineEdit2 = tk.Entry(self)
        self.lineEdit2.grid(row=1, column=1, padx=10, pady=10)

        self.lineEdit_resultado = tk.Entry(self, state='readonly')
        self.lineEdit_resultado.grid(row=2, column=1, padx=10, pady=10)
        self.lineEdit_resultado.insert(0, "0")

        # Botones 
        #Uso de sticky='nsew': Esto hace que los botones se expandan para llenar 
        # la celda en todas las direcciones (norte, sur, este y oeste).
        self.boton_sumar = tk.Button(self, text="+", command=self.sumar)
        self.boton_sumar.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
       
        self.boton_restar = tk.Button(self, text="-", command=self.restar)
        self.boton_restar.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

        self.boton_multiplicar = tk.Button(self, text="*", command=self.multiplicar)
        self.boton_multiplicar.grid(row=4, column=0, padx=10, pady=10, sticky='nsew' )

        self.boton_dividir = tk.Button(self, text="/", command=self.dividir)
        self.boton_dividir.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')

        self.boton_modulo = tk.Button(self, text="%", command=self.modulo)
        self.boton_modulo.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')

        self.boton_reset = tk.Button(self, text="RESET", command=self.reset)
        self.boton_reset.grid(row=5, column=1, padx=10, pady=10, sticky='nsew' )

    def sumar(self):
        num1 = float(self.lineEdit1.get())
        num2 = float(self.lineEdit2.get())
        resultado = num1 + num2
        self.lineEdit_resultado.config(state='normal')
        self.lineEdit_resultado.delete(0, tk.END)
        self.lineEdit_resultado.insert(0, str(resultado))
        self.lineEdit_resultado.config(state='readonly')

    def restar(self):
        num1 = float(self.lineEdit1.get())
        num2 = float(self.lineEdit2.get())
        resultado = num1 - num2
        self.lineEdit_resultado.config(state='normal')
        self.lineEdit_resultado.delete(0, tk.END)
        self.lineEdit_resultado.insert(0, str(resultado))
        self.lineEdit_resultado.config(state='readonly')

    def multiplicar(self):
        num1 = float(self.lineEdit1.get())
        num2 = float(self.lineEdit2.get())
        resultado = num1 * num2
        self.lineEdit_resultado.config(state='normal')
        self.lineEdit_resultado.delete(0, tk.END)
        self.lineEdit_resultado.insert(0, str(resultado))
        self.lineEdit_resultado.config(state='readonly')

    def dividir(self):
        num1 = float(self.lineEdit1.get())
        num2 = float(self.lineEdit2.get())
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Div/0"  # Manejo simple de división por cero
        self.lineEdit_resultado.config(state='normal')
        self.lineEdit_resultado.delete(0, tk.END)
        self.lineEdit_resultado.insert(0, str(resultado))
        self.lineEdit_resultado.config(state='readonly')

    def modulo(self):
        num1 = float(self.lineEdit1.get())
        num2 = float(self.lineEdit2.get())
        resultado = num1 % num2
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
