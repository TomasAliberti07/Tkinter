import tkinter as tk

class Peliculas(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Películas")
        self.configure(bg='LightGreen')
        # Etiqueta para el título
        self.label_title = tk.Label(self, text="Escribe el título de una película")
        self.label_title.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='w')

        # Etiqueta para la lista de películas
        self.label_list = tk.Label(self, text="Películas")
        self.label_list.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='w')

        # Campo de entrada para el nombre de la película
        self.entry_pelicula = tk.Entry(self)
        self.entry_pelicula.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        # Lista para mostrar las películas añadidas
        self.listbox_peliculas = tk.Listbox(self)
        self.listbox_peliculas.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Botón para añadir la película
        self.button_add = tk.Button(self, text="Añadir", command=self.add_pelicula)
        self.button_add.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
 
    def add_pelicula(self):
        pelicula = self.entry_pelicula.get()
        if pelicula:  # Verifica que no esté vacío
            self.listbox_peliculas.insert(tk.END, pelicula)
            self.entry_pelicula.delete(0, tk.END)  # Limpia el campo de entrada

# Crear la instancia de la aplicación y ejecutar el bucle principal
ventana = Peliculas()
ventana.mainloop()