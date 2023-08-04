'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Pedir:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

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

        postulantes_nb_asp_js_ssr = 0
        bandera_postulante_menor_edad = True
        edad_postulante_jr_menor_edad = 0
        nombre_postulante_menor_edad = ""
        acumulador_edad_F = 0 
        acumulador_edad_M = 0
        acumulador_edad_NB = 0
        contador_generos_F = 0
        contador_generos_M = 0
        contador_generos_NB = 0
        contador_postulantes_python = 0
        contador_postulantes_asp_net = 0
        contador_postulantes_js = 0
        tecnologia_mas_postulantes = ""


        for numero in range(10):

            nombre = prompt("Nombre", "Ingrese su nombre")
            while nombre is None or nombre == "" or nombre.isdigit(): # Is digit true es que contiene numeros
                nombre = prompt("Nombre", "*ERROR* Ingresaste mal tu nombre")

            while True:    
                edad = prompt("Edad", "Ingrese su edad:")
                if(edad != None and edad.isdigit()): # Que la edad, no sea NONE y contenga numeros is digit TRUE (Contiene numeros)
                    edad_entero = int(edad) # Si lo de arriba es verdadero, acá vamos a convertir a entero
                    if (edad_entero < 18):
                        alert("Edad", "ERROR!Debe ser mayor a 18")
                    else:
                        break
                else:
                    alert("Edad", "ERROR! Ingrese una edad correcta")

            genero_ingresado = prompt("Edad", "Ingrese su lenguaje:")
            while genero_ingresado != "F" and genero_ingresado != "M" and genero_ingresado != "NB":
                alert("ERROR FATAL ⚠","Has ingresado un Letra inexistente")
                genero_ingresado = prompt("","Ingrese su Letra correspondiente por favor")

            lenguaje_ingresado = prompt("Edad", "Ingrese su lenguaje:")
            while lenguaje_ingresado != "PYTHON" and lenguaje_ingresado != "JS" and lenguaje_ingresado != "ASP.NET":
                alert("ERROR FATAL ⚠","Has ingresado un lenguaje no aceptado")
                lenguaje_ingresado = prompt("","Ingrese su lenguaje correspondiente por favor")

            puesto_ingresado = prompt("Edad", "Ingrese su puesto:")
            while puesto_ingresado != "Jr" and puesto_ingresado != "Ssr" and puesto_ingresado != "Sr":
                alert("ERROR FATAL ⚠","Has ingresado un puesto inexistente")
                puesto_ingresado = prompt("","Ingrese su puesto correspondiente por favor")

            # SI LLEGO ACÁ LLEGARON LOS DATOS BIEN.

            #A
            if genero_ingresado == "NB":
                        match lenguaje_ingresado:
                            case "ASP.NET" | "JS":
                                if edad > 24 and edad < 41:
                                    if puesto_ingresado == "Ssr":
                                        postulantes_nb_asp_js_ssr += 1

            #B. Nombre del postulante Jr con menor edad.

            if puesto_ingresado == "Jr":
                if bandera_postulante_menor_edad == True:
                    edad_postulante_jr_menor_edad = edad_entero
                    nombre_postulante_menor_edad = nombre
                    bandera_postulante_menor_edad == False
                else:
                    if edad_postulante_jr_menor_edad > edad:
                        nombre_postulante_menor_edad = nombre 
                        edad_postulante_jr_menor_edad = edad_entero

            if puesto_ingresado == "Jr" and (bandera_postulante_menor_edad is True or edad < edad_postulante_jr_menor_edad):
                bandera_postulante_menor_edad = False
                edad_postulante_jr_menor_edad = edad
                nombre_postulante_menor_edad = nombre
            
            # C
            match genero_ingresado:
                case "F":
                    acumulador_edad_F += edad
                    contador_generos_F += 1
                case "M":
                    acumulador_edad_M += edad
                    contador_generos_M += 1

                case "NB":
                    acumulador_edad_NB += edad
                    contador_generos_NB += 1

            #D
            match lenguaje_ingresado:
                case "PYTHON":
                    contador_postulantes_python += 1
                case "ASP.NET":
                    contador_postulantes_asp_net += 1 
                case "JS":
                    contador_postulantes_js += 1

        # D
        if contador_postulantes_python > contador_postulantes_js and contador_postulantes_python > contador_postulantes_asp_net:
            tecnologia_mas_postulantes = "Python"
        elif contador_postulantes_js > contador_postulantes_asp_net and contador_postulantes_js > contador_postulantes_python:
            tecnologia_mas_postulantes = "JavaScript"
        else:
            tecnologia_mas_postulantes = "ASP.NET"


        promedio_edad_por_genero_m = acumulador_edad_M / contador_generos_M
        promedio_edad_por_genero_f = acumulador_edad_F / contador_generos_F
        promedio_edad_por_genero_nb = acumulador_edad_NB / contador_generos_NB 



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

