'''
Máximo y mínimo de algo
Validaciones "" isdigit isalpha 
Promedio
Porcentaje
Mostrar lista de datos
Más cartas posee
Romper bucle


########################  Máximo,más,caro,etc  ########################

bandera_primero=False
        for i in range (len(lista_nombre_carta_ur)):
            if bandera_primero==None or lista_nombre_carta_ur[i]>lista_precio_carta_ur[bandera_primero]:
                bandera_primero=i
        print(f"""La cantidad de cartas que se compraron de tipo Magica cuya rareza sea Ultra Rara y
            no hayan salido mas de 200 USD es: {contador_m_ur_menor_200} y el precio de la más cara es {lista_precio_carta_ur[bandera_primero]} 
            que es la carta {lista_nombre_carta_ur[i]}""")

        #indice_carta_mas_cara = None
        #indice_carta_menos_cara = None
        #maximo = None
        #minimo = None
        bandera_carta_mas_cara=False

        for i in range(len(self.nombre_carta)):
            if self.tipo_transaccion[i] == "compra":
                if self.rareza_carta[i] == "Ultra Rara":
                    if bandera_carta_mas_cara == False:
                        maximo = self.precio_carta[i]
                        minimo = self.precio_carta[i]
                        indice_carta_mas_cara = i
                        indice_carta_menos_cara = i
                        bandera_carta_mas_cara = True
                    else:
                        if self.precio_carta[i] > maximo:
                            maximo = self.precio_carta[i]
                            indice_carta_mas_cara = i
                        if self.precio_carta[i] < minimo:
                            minimo = self.precio_carta[i]
                            indice_carta_menos_cara = i

        print(f"La carta más cara es {self.nombre_carta[indice_carta_mas_cara]} con un valor de {maximo} y el tipo de carta es {self.tipo_carta[indice_carta_mas_cara]}")
        print(f"La carta más barata es {self.nombre_carta[indice_carta_menos_cara]} con un valor de {minimo} y el tipo de carta es {self.tipo_carta[indice_carta_menos_cara]}")

'''
'''
########################  Tipo de...que más/menos posee  ########################

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

'''
'''
########################  Porcentaje sobre total de .. ingresados  ########################
largo_lista=len(self.nombre_carta)
        contador_ur_monstruo=0
        for i in range(largo_lista):
            if self.rareza_carta[i]=="Ultra Rara" and self.tipo_carta[i]=="Monstruo":
                    contador_ur_monstruo+=1
        porcentaje_ur_monstruo=contador_ur_monstruo/largo_lista*100
        print(f"El porcentaje de cartas UR tipo monstruo sobre el total es {porcentaje_ur_monstruo}")

'''
'''
########################  Lista que supera al valor promedio  ########################
lista_cartas_mayor_al_promedio=[]
        largo_lista=len(self.nombre_carta)
        acumulador_cartas=0
        promedio_cartas_sobre_precio=acumulador_cartas/largo_lista
        if self.tipo_transaccion=="compra":
            acumulador_cartas+=self.precio_carta[i]
        for i in range (largo_lista):
            if self.precio_carta[i]>promedio_cartas_sobre_precio:
                lista_cartas_mayor_al_promedio.append(self.nombre_carta[i])
'''
'''
VALIDARRR
while True:
            nombre_de_carta=prompt("NOMBRE", "Ingrese el nombre de la carta:")
            if nombre_de_carta=="" or nombre_de_carta is None or nombre_de_carta.isdigit():
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

edad = prompt("Edad", "Ingrese su edad:")
                if(edad != None and edad.isdigit()): # Que la edad, no sea NONE y contenga numeros is digit TRUE (Contiene numeros)
                    edad_entero = int(edad) # Si lo de arriba es verdadero, acá vamos a convertir a entero
                    if (edad_entero < 18):
                        alert("Edad", "ERROR!Debe ser mayor a 18")
                    else:
                        break
                else:
                    alert("Edad", "ERROR! Ingrese una edad correcta")            
            
            
            
            '''

