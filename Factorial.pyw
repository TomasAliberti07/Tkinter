import tkinter as tk

class SacarFactorial(tk.Tk):
    def __init__(self):
        super().__init__()

        self.n = 1  # Valor inicial de n

        # Configurar el color de fondo de la ventana
        self.configure(bg='lightseagreen')
        self.resizable(False,False)
        self.title("Factorial")

        # Etiqueta para n
        self.label_n = tk.Label(self, text="n:", bg='lightseagreen')
        self.label_n.grid(row=0, column=0, padx=10, pady=10)

        # Campo de entrada para mostrar n (no editable)
        self.lineEdit_n = tk.Entry(self, state='readonly')
        self.lineEdit_n.grid(row=0, column=1, padx=10, pady=10)
        self.actualizar_lineEdit_n()  # Actualizar aquí

        # Etiqueta para el factorial de n
        self.label_fact = tk.Label(self, text="Factorial(n):", bg='lightseagreen')
        self.label_fact.grid(row=1, column=0, padx=10, pady=10)

        # Campo de entrada para mostrar el factorial (no editable)
        self.lineEdit_fact = tk.Entry(self, state='readonly')
        self.lineEdit_fact.grid(row=1, column=1, padx=10, pady=10)
        self.actualizar_lineEdit_fact()  # Actualizar aquí

        # Botón "Siguiente"
        self.btn_siguiente = tk.Button(self, text="Siguiente", command=self.calcular_y_mostrar_factorial)
        self.btn_siguiente.grid(row=2, columnspan=2, pady=10)

    def calcular_factorial_manual(self, n):
        # Función para calcular el factorial manualmente
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def actualizar_lineEdit_n(self):
        # Actualiza el campo de entrada para n
        self.lineEdit_n.config(state='normal')
        self.lineEdit_n.delete(0, tk.END)
        self.lineEdit_n.insert(0, str(self.n))
        self.lineEdit_n.config(state='readonly')

    def actualizar_lineEdit_fact(self):
        # Actualiza el campo de entrada para el factorial
        fact_n = self.calcular_factorial_manual(self.n)
        self.lineEdit_fact.config(state='normal')
        self.lineEdit_fact.delete(0, tk.END)
        self.lineEdit_fact.insert(0, str(fact_n))
        self.lineEdit_fact.config(state='readonly')

    def calcular_y_mostrar_factorial(self):
        # Incrementa n y actualiza los lineEdits
        self.n += 1
        self.actualizar_lineEdit_n()
        self.actualizar_lineEdit_fact()

# Crear la instancia de la aplicación y ejecutar el bucle principal
ventana = SacarFactorial()
ventana.mainloop()
