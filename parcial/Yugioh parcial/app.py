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
NOMBRE = 'Nat' # Completa tu nombre completo solo en esa variable

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
                            "Ra el Señor de los Dioses","Dragon Egipcio de Oscuridad","CARTA PRUEBA","CARTA PRUEBA 2"]
        
        self.tipo_carta = ["Trampa","Magica","Monstruo","Magica","Trampa","Magica","Monstruo","Trampa","Magica","Monstruo","Magica","Magica"]
        self.rareza_carta = ["Ultra Rara","Ultra Rara","UltraRara","Rara","Rara","Rara","Super Rara","Ultra Rara","Super Rara","Ultra Rara","Ultra Rara","Ultra Rara"]
        self.tipo_transaccion = ["compra","venta","compra","compra","venta","venta","compra","venta","compra","venta","compra","compra"]
        self.precio_carta = [1.500,2000,800,1000,300,1200,1800,2500,2200,1900,90,140]
        

    def btn_mostrar_todos_on_click(self):
        largo_lista = len(self.nombre_carta)
        for i in range(largo_lista):
            print(f"""Nombre: {self.nombre_carta[i]},
                Tipo de Carta: {self.tipo_carta[i]},
                Rareza: {self.rareza_carta[i]},
                Tipo de transaccion: {self.tipo_transaccion[i]},
                Precio: {self.precio_carta[i]}""")

    def btn_mostrar_informe_1(self):
        #! 0) - Cantidad de Cartas que se compraron de tipo Magica cuya rareza sea Ultra Rara y no hayan salido mas de 200 USD 
        #(Agregar aumento de 10% para contemplar compras). 
        #(Agregar los nombres y precios de dichas cartas a las listas nuevas correspondientes)
        contador_m_ur_menor_200=0
        contador_rara=0
        contador_ultra_rara=0
        contador_super_rara=0
        contador_trampa=0
        contador_monstruo=0
        contador_magica=0
        contador_cartas_generales=0 
        contador_ur_monstruo=0
        contador_carta_monstruo_r_menor_50=0
        acumulador_valores_cartas=0
        lista_cartas_mayor_al_promedio=[]
        lista_precio_carta_ur=[]
        lista_nombre_carta_ur=[]

        largo_lista = len(self.nombre_carta)
        for i in range(largo_lista):
            contador_cartas_generales+=1
            if self.tipo_transaccion[i]=="compra":
                if self.tipo_carta[i]=="Magica":
                    if self.rareza_carta[i]=="Ultra Rara":
                        if self.precio_carta[i]*1.10 <= 200:
                            contador_m_ur_menor_200+=1
                            lista_nombre_carta_ur.append(self.nombre_carta[i])
                            lista_precio_carta_ur.append(self.precio_carta[i])
                            print(lista_nombre_carta_ur)
                            print(lista_precio_carta_ur)
            match self.rareza_carta[i]:
                case "Rara":
                    contador_rara+=1
                case "Ultra Rara":
                    contador_ultra_rara+=1
                case _:
                    contador_super_rara+=1
        #! 9) - De las listas (realizada en el informe 0) averiguar, cual es la mas cara de estas y luego
        #contar la cantidad que sean para mostrar un mensaje que sea.
        bandera_primero=False
        for i in range (len(lista_nombre_carta_ur)):
            if bandera_primero==None or lista_nombre_carta_ur[i]>lista_precio_carta_ur[bandera_primero]:
                bandera_primero=i
        print(f"""La cantidad de cartas que se compraron de tipo Magica cuya rareza sea Ultra Rara y
            no hayan salido mas de 200 USD es: {contador_m_ur_menor_200} y el precio de la más cara es {lista_precio_carta_ur[bandera_primero]} 
            que es la carta {lista_nombre_carta_ur[i]}""")
        print(f"Cartas raras: {contador_rara}, super rara: {contador_super_rara} y ultra rara: {contador_ultra_rara}")
        #! 1) - Rareza de las cartas que menos cartas posea. 
        if contador_rara<contador_ultra_rara and contador_rara<contador_super_rara:
            menos_rara="Rara"
        elif contador_super_rara<contador_ultra_rara:
            menos_rara="Super Rara"
        else:
            menos_rara="Ultra Rara"
        #! 2) - Tipo de los cartas que mas cartas posea.
        match self.tipo_carta[i]:
                case "Magica":
                    contador_magica+=1
                case "Monstruo":
                    contador_monstruo+=1
                case _:
                    contador_trampa+=1

        if contador_magica<contador_monstruo and contador_magica<contador_trampa:
            tipo_mas_posee="Magica"
        elif contador_trampa<contador_monstruo:
            tipo_mas_posee="Trampa"
        else:
            tipo_mas_posee="Monstruo"
        #! 3) - Porcentaje de cartas de rareza Ultra Rara de tipo mounstro (Sobre el total de cartas ingresadas).
        if self.rareza_carta[i]=="Ultra Rara" and self.tipo_carta[i]=="Monstruo":
                contador_ur_monstruo+=1
        porcentaje_ur_monstruo=contador_ur_monstruo/largo_lista*100
        #! 4) - Nombre y tipo de la carta que se compró con la rareza Ultra rara del costo mas elevado.
        bandera_segundo=False
        if self.rareza_carta[i]=="Ultra Rara":
            if self.tipo_transaccion[i]=="compra":
                for i in range (len(lista_nombre_carta_ur)):
                    if bandera_segundo==None or self.precio_carta[i]>self.precio_carta[bandera_segundo]:
                        bandera_segundo=i
        print(f"El nombre: {self.nombre_carta[bandera_segundo]} y el tipo es: {self.tipo_carta[bandera_segundo]}")
        #! 5) - Porcentaje de cartas de tipo monstruo con rareza rara que haya salido igual o menor USD 50 (sobre el total de cartas ingresadas).
        if self.tipo_carta=="Monstruo":
            if self.rareza_carta=="Rara":
                if self.precio_carta<=50:
                    contador_carta_monstruo_r_menor_50+=1

        porcentaje_rara_monstruo=contador_carta_monstruo_r_menor_50/largo_lista*100
        #! 6) - Listado de todas las cartas cuyo poder de valor de compra supere el valor promedio.
        promedio_cartas_sobre_precio=acumulador_valores_cartas/largo_lista
        if self.tipo_transaccion=="compra":
            acumulador_valores_cartas+=self.precio_carta[i]
        for i in range (largo_lista):
            if self.precio_carta[i]>promedio_cartas_sobre_precio:
                lista_cartas_mayor_al_promedio.append(self.nombre_carta[i])
        #! 7) - Cantidad de Cartas que se vendieron de tipo trampa cuya rareza sea rara y se hayan vendido entre al menos los 100 y 300 dolares
        #(Contemplar el 10% de descuento por comisión de ventas).
        if self.tipo_transaccion[i]=="venta":
            if self.tipo_carta[i]=="Trampa":
                if self.rareza_carta[i]=="Rara":
                    if self.precio_carta[i]*0.90>=100 and self.precio_carta[i]*0.90<=300:
                        contador_cartas_trampa_rara_100y300+=1
        #! 8) - Nombre y tipo de la carta que se vendió con la rareza Super Rara del costo mas bajo.
        bandera_tercero=None
        if self.rareza_carta[i]=="Super Rara":
            if self.tipo_transaccion[i]=="venta":
                    if bandera_tercero==None or self.precio_carta[i]<self.precio_carta[bandera_tercero]:
                        bandera_tercero=i
        print(f"El nombre: {self.nombre_carta[bandera_tercero]} y el tipo es: {self.tipo_carta[bandera_tercero]}")






    def btn_mostrar_informe_2(self):
        pass

    def btn_mostrar_informe_3(self):
        pass 

    def btn_cargar_cartas_on_click(self):
        while True:
            nombre_de_carta=prompt("NOMBRE", "Ingrese el nombre de la carta:")
            while nombre_de_carta=="" or nombre_de_carta.isdigit():
                nombre_de_carta=prompt("ERROR", "Reingrese el nombre de la carta:")
            self.nombre_carta.append(nombre_de_carta)

            tipo_de_carta=prompt("TIPO DE CARTA", "Ingrese el tipo de carta:")
            while (tipo_de_carta != "Monstruo" and tipo_de_carta != "Magica" and  tipo_de_carta != "Trampa"):
                tipo_de_carta=prompt("ERROR", "Reingrese el tipo de carta:")
            self.tipo_carta.append(tipo_de_carta)

            tipo_de_transaccion=prompt("TIPO DE TRANSACCIÓN", "Ingrese el tipo de transacción:")
            while (tipo_de_transaccion != "compra" and tipo_de_transaccion != "venta"):
                tipo_de_carta=prompt("ERROR", "Reingrese el tipo de transacción:")
            self.tipo_transaccion.append(tipo_de_transaccion)

            tipo_de_rareza=prompt("TIPO DE RAREZA", "Ingrese el tipo de rareza de la carta:")
            while (tipo_de_rareza != "Rara" and tipo_de_rareza != "Super Rara" and  tipo_de_rareza != "Ultra Rara"):
                tipo_de_carta=prompt("ERROR", "Reingrese el tipo de rareza de la carta:")
            self.rareza_carta.append(tipo_de_rareza)

            precio_de_carta=prompt("PRECIO", "Ingrese el precio de la carta:")
            while int(precio_de_carta)<=0:
                precio_de_carta=prompt("ERROR", "Reingrese el precio de la carta:")
            self.precio_carta.append(precio_de_carta)

            carga_datos=question("DATOS", "Desea seguir ingresando las cartas?")
            if carga_datos==False:
                break





if __name__ == "__main__":
    app = App()
    app.mainloop()
