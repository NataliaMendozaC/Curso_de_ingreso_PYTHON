import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador=0
        acumulador=0
        acumulador_negativos=0
        contador_negativos=0
        acumulador_positivos=0
        contador_positivos=0
        contador_ceros=0

        while True:
            numero_ingresado=prompt("numero", "Ingrese un número: ")
            if numero_ingresado==None:
                break
            numero=int(numero_ingresado)
            acumulador+=numero
            contador+=1

            if numero<0:
                acumulador_negativos+=numero
                contador_negativos+=1
            elif numero>0:
                acumulador_positivos+=numero
                contador_positivos+=1
            else:
                contador_ceros+=1

        diferencia=contador_positivos-contador_negativos
        alert("",f"La cantidad de numeros negati mvos ingresados es {contador_negativos} y la suma de estos es {acumulador_negativos}")
        alert("",f"La cantidad de numeros positivos ingresados es {contador_positivos} y la suma de estos es {acumulador_positivos}")
        alert("",f"La cantidad de ceros que se ingresó es {contador_ceros}")
        alert("",f"La diferencia entre la cantidad de los números positivos ingresados y los negativos es {diferencia}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
