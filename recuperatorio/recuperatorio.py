# Copyright (C) 2023 <UTN FRA>
# 
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
NOMBRE = 'Natalia Mendoza' # Completa tu nombre completo solo en esa variable

"""
A) Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que el decida.

    * (VALIDAR) Nombre de la carta: No puede estar vacio.
    * (VALIDAR) Tipo de carta: "Monstruo", "Magica", "Trampa".
    * (VALIDAR) Tipo de transacción: "Compra", "Venta".
    * (VALIDAR) Rareza: Que sea "Rara", "Super Rara", "Ultra Rara".
    * (VALIDAR) Precio: Que no sea 0 o negativo.
    * (VALIDAR) Ataque de carta : que no sea negativo y debe ser mayor a 20
    * (VALIDAR) Color de carta: "rojo","blanco","negro"

B)
    Al presionar el boton mostrar se deberan listar todas las cartas con la siguiente información:
    *Nombre - Tipo de carta - Tipo de transacción - Rareza - Precio - ataque de cartas - color de carta.

C) Solo debera realizar 4 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    

    Informe 1- Realizar el ultimo numero de su DNI Personal (Ej 4) (Si es 0 o 9) (si es 9 hacer el 7, si es 0 hacer el 3)

    INFORME 2: Realizar informe (0 y 9 - OBLIGATORIO)

    Informe 3- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 4.
    

Realizar los informes correspondientes a los numeros obtenidos u informes obligatorios. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 

    #! 0) - Cantidad de Cartas que se compraron de tipo trampa de color negro y hayan salido mas de 1000 USD 
    (Agregar aumento de 10% para contemplar compras). 
    (Agregar los nombres y precios de dichas cartas a las listas nuevas correspondientes)

    #! 1) - Rareza de las cartas ,que sean rojo que menos cartas posea. 
    #! 2) - Tipo de las cartas ,que sean blanco mas cartas posea. 
    #! 3) - promedio de cartas que su ataque sea 30 o superior.
    #! 4) - Nombre y rareza de la carta que tiene mas ataque
    #! 5) - Porcentaje de cartas de tipo magica con que su ataque sea 30 o inferior (sobre el total de cartas ingresadas).
    #! 6) - Listado de todas las cartas cuyo poder de valor de compra supere el ataque promedio.
    #! 7) - Cantidad de Cartas que se vendieron de rojo y blanco cuya tipo sea monstruo y se hayan vendido entre al menos los 150 y 500 dolares
    (Contemplar el 10% de descuento por comisión de ventas).
    #! 8) - Nombre y rareza de la carta que tiene menos ataque
    #! 9) - De las listas (realizada en el informe 0) averiguar, cual es la mas barata de estas y luego
            contar la cantidad que sean para mostrar un mensaje que sea.
    Ej: De las cartas de tipo trampa , con color negro y con un valor mayor a USD 1000 tenemos un total (x) y la mas  es: (x).

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
                            "Ra el Señor de los Dioses","Dragon Egipcio de Oscuridad"]
        
        self.tipo_carta = ["Trampa","Magica","Monstruo","Magica","Trampa","Magica","Monstruo","Trampa","Magica","Monstruo"]
        self.rareza_carta = ["Ultra Rara","Ultra Rara","UltraRara","Rara","Rara","Rara","Super Rara","Ultra Rara","Super Rara","Ultra Rara"]
        self.tipo_transaccion = ["compra","venta","compra","compra","venta","venta","compra","venta","compra","venta"]
        self.precio_carta = [1.500,2000,800,1000,300,1200,1800,2500,2200,1900,1500]
        self.color_carta = ["rojo","negro","blanco","negro","negro","blanco","rojo","rojo","blanco","blanco",]
        self.ataque_cartas = [48,23,12,31,20,35,40,50,28,50,]
        
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        
    def btn_mostrar_todos_on_click(self):
        largo_lista = len(self.nombre_carta)
        for i in range(largo_lista):
            print(f"""Nombre de la carta: {self.nombre_carta[i]}. Tipo de carta: {self.tipo_carta[i]}. Tipo de rareza: {self.rareza_carta[i]}. 
            Tipo de transacción: {self.tipo_transaccion[i]}. Precio de la carta: {self.precio_carta[i]}. Color de carta: {self.color_carta[i]}.
            Ataque carta: {self.ataque_cartas[i]}
            """)

    def btn_mostrar_informe_1(self):
        contador_magica=0
        contador_monstruo=0
        contador_trampa=0
        for i in range(len(self.nombre_carta)):
            if self.color_carta[i]=="blanco":
                match self.tipo_carta[i]:
                    case "Magica":
                        contador_magica+=1
                    case "Monstruo":
                        contador_monstruo+=1
                    case _:
                        contador_trampa+=1

        if contador_monstruo>contador_magica and contador_monstruo>contador_trampa:
            tipo_mas_posee="Montruo"
        elif contador_magica>contador_trampa:
            tipo_mas_posee="Magica"
        else:
            tipo_mas_posee="Trampa"

        print(f"El tipo de cartas que más posee es {tipo_mas_posee}.")

    def btn_mostrar_informe_2(self):
        contador_carta_trampa_negro=0
        lista_nombres=[]
        lista_precios=[]
        bandera_primero=False
        for i in range(len(self.nombre_carta)):
            if self.tipo_transaccion[i]=="compra":
                if self.tipo_carta=="Trampa":
                    if self.color_carta=="negro":
                        if self.precio_carta*1.10>=1000:
                            contador_carta_trampa_negro+=1
                            lista_nombres.append(self.nombre_carta[i])
                            lista_precios.append(self.precio_carta[i])

        for i in range (len(lista_nombres)):
            if bandera_primero==None or lista_nombres[i]<lista_precios[bandera_primero]:
                bandera_primero=i
        print(f"""Cantidad cartas que se compraron de tipo trampa color negro: {contador_carta_trampa_negro}. El precio de la más barata es {lista_precios[bandera_primero]} 
            que es la carta {lista_nombres[i]}""")
        


    def btn_mostrar_informe_3(self):
        pass 
        #! 7) - Cantidad de Cartas que se vendieron de rojo y blanco cuya tipo sea monstruo y se hayan vendido entre al menos los 150 y 500 dolares
        #(Contemplar el 10% de descuento por comisión de ventas).
        contador_cartas_rojo_blanco_monstruo=0
        for i in range(len(self.nombre_carta)):
            if self.tipo_transaccion[i]=="venta":
                if self.color_carta[i]=="rojo" or self.color_carta=="blanco":
                    if self.tipo_carta[i]=="Monstruo":
                        if self.precio_carta*0.90>=150 and self.precio_carta*0.90<=300:
                            contador_cartas_rojo_blanco_monstruo+=1
        print(f"La cantidad de cartas que se vendieron de rojo y blanco cuya tipo sea monstruo y se hayan vendido entre al menos los 150 y 500 dolares es: {contador_cartas_rojo_blanco_monstruo} ")

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

            ataque_de_carta=prompt("ATAQUE", "Ingrese el tipo de ataque:")
            while int(ataque_de_carta)<=20:
                ataque_de_carta=prompt("ERROR", "Reingrese el tipo de ataque:")
            self.ataque_cartas.append(ataque_de_carta)

            color_de_carta=prompt("COLOR", "Ingrese el color de su carta:")
            while (color_de_carta != "rojo" and color_de_carta != "blanco" and  color_de_carta != "negro"):
                tipo_de_carta=prompt("ERROR", "Reingrese el color de su carta:")
            self.color_carta.append(color_de_carta)

            pregunta=question("", "Desea continuar ingresando datos?")
            if pregunta==False:
                break

if __name__ == "__main__":
    app = App()
    app.mainloop()


