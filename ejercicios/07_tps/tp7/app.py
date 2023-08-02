'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        cantidad_NB=0

        for numero in range (2):
            nombre=prompt("Nombre", "Ingrese su nombre: ")
            while nombre=="" and nombre.isdigit==True:
                nombre=prompt("error", "ERROR: Nombre inválido, vuelva a ingresarlo.")
            while True:
                edad=prompt("Edad", "Ingrese su edad")
                if edad.isdigit():
                    edad_entero=int(edad)
                    if edad_entero>=18:
                        break
                    else:
                        alert("error","ERROR: La edad debe ser mayor o igual a 18.")
                else:
                    alert("error", "ERROR: Ingrese una edad válida (solo números enteros).")
            genero=prompt("Género", "Ingrese su género teniendo en cuenta F - M - NB")
            tecnologia=prompt("Tecnología", "Ingrese en qué tecnología se desarrolla: PYTHON - JS - ASP.NET")
            puesto=prompt("Puesto", "Puesto al que se postula: Jr - Ssr - Sr")
            mensaje=f"Su nombre es {nombre}, su edad {edad} años y su género {genero}. La tecnología en la que se desarrolla es {tecnologia} y su postulación es para el puesto de {puesto}."
            alert("", mensaje)

            if genero == 'NB' and (tecnologia == 'ASP.NET' or tecnologia == 'JS') and 25 <= edad <= 40 and puesto == 'Ssr':
                cantidad_NB += 1

            alert("", cantidad_NB)

            alert=("", cantidad_NB)



        
            




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
