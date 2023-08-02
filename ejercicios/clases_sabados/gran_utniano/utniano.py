import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:Natalia
Apellido:Mendoza
Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_nombres = ["Camila","Matias","Marcos","Lucas","Lucia", "Natalia"]
        self.lista_edades = [14,48,35,29,21,55]
        self.lista_genero = ["Femenino","Masculino","Otro","Masculino","Femenino","Otro"]
        self.lista_participantes = ["Giovanni","Gianni","Facundo","Giovanni","Gianni","Facundo"]


    def btn_mostrar_on_click(self):
        #A- El promedio de la edad de los votantes ge género  Femenino
        contador_femenino=0
        acumulador_femenino=0
        for i in range(len(self.lista_edades)):
            if self.lista_genero[i] == "Femenino":
                acumulador_femenino += self.lista_edades[i]
                contador_femenino += 1

        if contador_femenino>=1:
            promedio_edad_femenino= acumulador_femenino/contador_femenino
        else:
            promedio_edad_femenino="No hubo votantes femeninos."

        print(promedio_edad_femenino)

        #B- Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo
        contador_masculino=0
        for i in range(len(self.lista_edades)):
            if (self.lista_genero[i] == "Masculino" and 
                self.lista_edades[i] >24 and self.lista_edades[i] <41 and
                self.lista_participantes[i]== "Giovanni" or self.lista_participantes[i]== "Facundo"):
                        contador_masculino += 1

        print(contador_masculino)

            #if self.lista_genero[i] == "Masculino":
                #if self.lista_edades[i] >24 and self.lista_edades[i] <41:
                    #if self.lista_participantes[i]== "Giovanni" or self.lista_participantes[i]== "Facundo":
                        #contador_masculino += 1

        #C- Nombre del votante más joven que votó a Gianni
        edad_min=None
        votante_joven=None
        for i in range (len(self.lista_participantes)):
             if self.lista_participantes[i] == "Gianni":
                  if edad_min==None or self.lista_edades[i]<edad_min:
                       edad_min = self.lista_edades[i]
                       votante_joven=self.lista_edades[i]

        print(votante_joven)
            


        
    def btn_cargar_on_click(self):
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()