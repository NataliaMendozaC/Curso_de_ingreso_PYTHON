import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Piedra, Papel o Tijera (v 1.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
	El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió
'''

class App(customtkinter.CTk):
     
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_piedra = customtkinter.CTkButton(master=self, text="Piedra", command=self.btn_piedra_on_click)
        self.btn_piedra.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_papel = customtkinter.CTkButton(master=self, text="Papel", command=self.btn_papel_on_click)
        self.btn_papel.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_tijera = customtkinter.CTkButton(master=self, text="Tijera", command=self.btn_tijera_on_click)
        self.btn_tijera.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_restart = customtkinter.CTkButton(master=self, text="RESTART", command=self.btn_restart_on_click, fg_color="red")
        self.btn_restart.grid(row=5, pady=20, columnspan=2, sticky="nsew")
        
        self.cpu_elije()
        print(self.seleccion_cpu)
        

    def cpu_elije(self):
        numero = random.randrange(1, 3)  # 1 Piedra / 2 Papel / 3 Tijera
        match(numero):
            case 1: 
                self.seleccion_cpu = "Piedra"
            case 2: 
                self.seleccion_cpu = "Papel"
            case 3: 
                self.seleccion_cpu = "Tijera"


    def deshabilitar_botones(self):
        pass

    def btn_restart_on_click(self):
        pass

    def btn_piedra_on_click(self):
        pass

    def btn_papel_on_click(self):
        pass

    def btn_tijera_on_click(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()