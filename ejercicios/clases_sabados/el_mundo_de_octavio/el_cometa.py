import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa 🪁", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)
        
        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        diametro_menor = self.txt_diametro_menor.get()
        lados_menores = self.txt_lados_menores.get()
        lados_mayores = self.txt_lados_mayores.get()

        diametro_menor_float = float(diametro_menor)
        lados_menores_float = float(lados_menores)
        lados_mayores_float = float(lados_mayores)

        cateto_df = (diametro_menor_float / 2) 
        mitad_grande_diametro_mayor = round((lados_mayores_float**2 - cateto_df**2) **0.5, 2)
        mitad_chica_diametro_mayor = round((lados_menores_float**2 - cateto_df**2) **0.5, 2)
        diametro_mayor = round(mitad_chica_diametro_mayor + mitad_grande_diametro_mayor, 2)
        

        perimetro = 2*(lados_menores_float + lados_mayores_float)
        perimetro_total = perimetro + diametro_menor_float + diametro_mayor

        area = (diametro_mayor * diametro_menor_float) / 2
        area_total = area * 1.10

        varillas_total = perimetro_total * 10
        papel_total = area_total * 10 

        varillas_total_mts = varillas_total / 100
        papel_total_mts = papel_total / 10000

        mensaje = "El total de metros de varillas es de {0}, y el total de papel es de {1:.2f} metros cuadrados.".format(varillas_total_mts, papel_total_mts)
        alert("Totales", mensaje)


    
if __name__ == "__main__":
    app = App()
    app.mainloop()