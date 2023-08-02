import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

#Nombre:Natalia
#Apellido:Mendoza

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour 🚂", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
        nombre=prompt("Nombre","¿Cuál es su nombre?")
        while type(nombre) is not str or nombre=="":
            alert("ERROR", "Ingrese un nombre válido.")
            nombre=prompt("Nombre","¿Cuál es su nombre?")

        edad=int(prompt("Edad","Ingrese su edad"))
        genero=prompt("Género","Ingrese su género: Masculino, Femenino u Otro.")
        altura=int(prompt("Altura","Ingrese su alt s{tura en centímetros, por ej: si usted mide 1,60cm ingrese 160."))

        if altura<=140:
            mensaje_altura="Baja."
        elif altura<=170:
            mensaje_altura="Media."
        elif altura<=190:
            mensaje_altura="Alta."
        else:
            mensaje_altura="Muy alta"

        mensaje="Usted es {0}, tiene {1} años de edad y su género es {2}.Usted mide {3}cm significa que su altura es {4}".format(nombre,edad,genero,altura,mensaje_altura)

        alert("Datos", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()