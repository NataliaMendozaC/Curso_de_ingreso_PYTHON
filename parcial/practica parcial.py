# PRACTICAR
# 0,2,7,9,verificación
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


"""
El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
Desea ingresar en el sistema las ventas realizadas en el dia de la fecha y conocer ciertos datos en base a las cartas que se vendieron.
"""
NOMBRE = 'Nata' # Completa tu nombre completo solo en esa variable

"""
A) Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que el decida.

    * (VALIDAR) Nombre de la carta: No puede estar vacio.
    * (VALIDAR) Tipo de carta: "Monstruo", "Magica", "Trampa".
    * (VALIDAR) Tipo de transacción: "Compra", "Venta".
    * (VALIDAR) Rareza: Que sea "Rara", "Super Rara", "Ultra Rara".
    * (VALIDAR) Precio: Que no sea 0 o negativo.

B)
    Al presionar el boton mostrar se deberan listar todas las cartas con la siguiente información:
    *Nombre - Tipo de carta - Tipo de transacción - Rareza - Precio.

C) Solo debera realizar 4 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    

    Informe 1- Realizar el ultimo numero de su DNI Personal (Ej 4) (Si es 0 o 9) (si es 9 hacer el 7, si es 0 hacer el 3)

    INFORME 2: Realizar informe (0 y 9 - OBLIGATORIO)

    Informe 3- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 4.
    

Realizar los informes correspondientes a los numeros obtenidos u informes obligatorios. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 

    #! 0) - Cantidad de Cartas que se compraron de tipo Magica cuya rareza sea Ultra Rara y no hayan salido mas de 200 USD 
    (Agregar aumento de 10% para contemplar compras). 
    (Agregar los nombres y precios de dichas cartas a las listas nuevas correspondientes)

    #! 1) - Rareza de las cartas que menos cartas posea. 
    #! 2) - Tipo de los cartas mas cartas posea. 
    #! 3) - Porcentaje de cartas de rareza Ultra Rara de tipo mounstro (Sobre el total de cartas ingresadas).
    #! 4) - Nombre y tipo de la carta que se compró con la rareza Ultra rara del costo mas elevado.
    #! 5) - Porcentaje de cartas de tipo mounstro con rareza rara que haya salido igual o menor USD 50 (sobre el total de cartas ingresadas).
    #! 6) - Listado de todas las cartas cuyo poder de valor de compra supere el valor promedio.
    #! 7) - Cantidad de Cartas que se vendieron de tipo trampa cuya rareza sea rara y se hayan vendido entre al menos los 100 y 300 dolares
    (Contemplar el 10% de descuento por comisión de ventas).
    #! 8) - Nombre y tipo de la carta que se vendió con la rareza Super Rara del costo mas bajo.
    #! 9) - De las listas (realizada en el informe 0) averiguar, cual es la mas cara de estas y luego
            contar la cantidad que sean para mostrar un mensaje que sea.
    Ej: De las cartas Magicas de rareza UR con un valor menor a USD 200 tenemos un total (x) y la mas cara es: (x).

"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Tienda de Yu-gi-oh! de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Tienda de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_cartas_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        

    
        self.nombre_carta = ["Dragón Blanco de Ojos Azules","Exodia el Prohibido","Mago Oscuro",
                            "Ciber Dragón","Hada Madrina","Dragón Negro de Ojos Rojos",
                            "Slifer el Dragón del Cielo","Obelisco el Atormentador",
                            "Ra el Señor de los Dioses","Dragon Egipcio de Oscuridad","carta prueba 1","carta prueba 2","carta prueba 3","carta prueba 4"]
        
        self.tipo_carta = ["Trampa","Magica","Monstruo","Magica","Trampa","Magica","Monstruo","Trampa","Magica","Monstruo","Magica","Magica","Magica","Trampa"]
        self.rareza_carta = ["Ultra Rara","Ultra Rara","Ultra Rara","Rara","Rara","Rara","Super Rara","Ultra Rara","Super Rara","Ultra Rara","Ultra Rara","Ultra Rara","Ultra Rara","Rara"]
        self.tipo_transaccion = ["compra","venta","compra","compra","venta","venta","compra","venta","compra","venta","compra","compra","compra","venta"]
        self.precio_carta = [1.500,2000,800,1000,100,1200,1800,2500,2200,1900,77,128,3,200]
        

    def btn_mostrar_todos_on_click(self):
        largo_lista=len(self.nombre_carta)
        for i in range (largo_lista):
            print(f"""Nombre de la carta: {self.nombre_carta[i]}. Tipo de carta: {self.tipo_carta[i]}
            Tipo de transacción: {self.tipo_transaccion[i]}. Rareza: {self.rareza_carta[i]}. Precio: {self.precio_carta[i]}
            """)

    def btn_mostrar_informe_1(self):
        #! 2) - Tipo de los cartas mas cartas posea. 
        contador_trampa=0
        contador_magica=0
        contador_monstruo=0

        match self.tipo_carta:
            case "Monstruo":
                contador_monstruo+=1
            case "Trampa":
                contador_trampa+=1
            case _:
                contador_magica+=1

        if contador_monstruo>contador_magica and contador_monstruo>contador_trampa:
            tipo_mas_posee="Montruo"
        elif contador_magica>contador_trampa:
            tipo_mas_posee="Magica"
        else:
            tipo_mas_posee="Trampa"

        print(f"El tipo de cartas que más posee es {tipo_mas_posee}.")


    def btn_mostrar_informe_2(self):
        #! 0) - Cantidad de Cartas que se compraron de tipo Magica cuya rareza sea Ultra Rara y no hayan salido mas de 200 USD 
        #(Agregar aumento de 10% para contemplar compras). 
        #(Agregar los nombres y precios de dichas cartas a las listas nuevas correspondientes)
        #! 9) - De las listas (realizada en el informe 0) averiguar, cual es la mas cara de estas y luego contar la cantidad que sean para mostrar un mensaje que sea.
        lista_nombre=[]
        lista_precios=[]
        contador_carta_magica_ur_menor_200=0
        largo_lista=len(self.nombre_carta)
        bandera_carta_mas_cara=False

        for i in range(largo_lista):
            if self.tipo_transaccion[i]=="compra":
                if self.tipo_carta[i]=="Magica":
                    if self.rareza_carta[i]=="Ultra Rara":
                        if self.precio_carta[i]*1.10<=200:
                            contador_carta_magica_ur_menor_200+=1
                            lista_nombre.append(self.nombre_carta[i])
                            lista_precios.append(self.precio_carta[i])

        print(f"La cantidad de cartas que se compraron tipo Magica UR con precio menor a $200 es: {contador_carta_magica_ur_menor_200}")
        #for i in range (len(lista_nombre)):
            #print(f"Una de las cartas que tiene estas características es: {lista_nombre[i]} con un valor de {lista_precios[i]}")
        indice_carta_mas_cara = None
        indice_carta_menos_cara = None
        for i in range (len(lista_nombre)):
            print(f"Una de las cartas que tiene estas características es: {lista_nombre[i]} con un valor de {lista_precios[i]}")
            if bandera_carta_mas_cara==False:
                maximo=lista_precios[i]
                minimo=lista_precios[i]
                indice_carta_mas_cara = i
                indice_carta_menos_cara = i
                bandera_carta_mas_cara=True
            else:
                if lista_precios[i]>maximo:
                    maximo=lista_precios[i]
                    indice_carta_mas_cara = i
                if lista_precios[i]<minimo:
                    minimo=lista_precios[i]
                    indice_carta_menos_cara = i
            #print(f"La carta más cara es {lista_nombre[i]} con un valor de {maximo[i]}")
        print(f"La carta más cara es {lista_nombre[indice_carta_mas_cara]} con un valor de {maximo}")
        print(f"La carta más barata es {lista_nombre[indice_carta_menos_cara]} con un valor de {minimo}")

        



    def btn_mostrar_informe_3(self):
        #! 7) - Cantidad de Cartas que se vendieron de tipo trampa cuya rareza sea rara y se hayan vendido entre al menos los 100 y 300 dolares
        #(Contemplar el 10% de descuento por comisión de ventas).
        contador_carta_trampa_r_entre_100_300=0
        for i in range (len(self.nombre_carta)):
            if self.tipo_transaccion[i]=="venta":
                if self.tipo_carta[i]=="Trampa":
                    if self.rareza_carta[i]=="Rara":
                        if self.precio_carta[i]*0.90>=100 and self.precio_carta[i]*0.90<=300:
                            contador_carta_trampa_r_entre_100_300+=1

        print(f"La cantidad de cartas que se vendieron tipo trampa rara entre $100 y $300 es: {contador_carta_trampa_r_entre_100_300}")


    def btn_cargar_cartas_on_click(self):
        while True:

            nombre_de_carta=prompt("NOMBRE", "Ingrese el nombre de la carta:")
            if nombre_de_carta=="":
                nombre_de_carta=prompt("ERROR", "Reingrese el nombre de la carta:")
            self.nombre_carta.append(nombre_de_carta)

            tipo_de_carta=prompt("TIPO", "Ingrese un tipo de carta:")
            while (tipo_de_carta != "Monstruo" and tipo_de_carta != "Magica" and  tipo_de_carta != "Trampa"):
                tipo_de_carta=prompt("ERROR", "Reingrese un tipo de carta:")
            self.tipo_carta.append(tipo_de_carta)

            tipo_de_transaccion=prompt("TRANSACCION", "Ingrese un tipo de transacción:")
            while (tipo_de_transaccion != "venta" and tipo_de_transaccion != "compra"):
                tipo_de_transaccion=prompt("ERROR", "Reingrese un tipo de transacción:")
            self.tipo_transaccion.append(tipo_de_transaccion)

            tipo_de_rareza=prompt("RAREZA", "Ingrese un tipo de rareza:")
            while (tipo_de_rareza != "Rara" and tipo_de_rareza != "Super Rara" and  tipo_de_rareza != "Ultra Rara"):
                tipo_de_carta=prompt("ERROR", "Reingrese un tipo de rareza:")
            self.rareza_carta.append(tipo_de_rareza)

            precio_de_carta=prompt("PRECIO","Ingrese el precio de la carta:")
            while int(precio_de_carta)<=0:
                precio_de_carta=prompt("ERROR","Reingrese el precio de la carta:")
            self.precio_carta.append(precio_de_carta)

            pregunta=question("DATOS", "Desea cargar otra carta?")
            if pregunta==False:
                break


if __name__ == "__main__":
    app = App()
    app.mainloop()