"""
EJERCICIO:
¡Disney ha presentado un montón de novedades en su D23! 
Pero... ¿Dónde está Mickey?
Mickey Mouse ha quedado atrapado en un laberinto mágico 
creado por Maléfica.
Desarrolla un programa para ayudarlo a escapar.
Requisitos:
1. El laberinto está formado por un cuadrado de 6x6 celdas.
2. Los valores de las celdas serán:
    - ⬜️ Vacío
    - ⬛️ Obstáculo
    - 🐭 Mickey
    - 🚪 Salida
Acciones:
1. Crea una matriz que represente el laberinto (no hace falta
que se genere de manera automática).
2. Interactúa con el usuario por consola para preguntarle hacia
donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
3. Muestra la actualización del laberinto tras cada desplazamiento.
4. Valida todos los movimientos, teniendo en cuenta los límites
del laberinto y los obtáculos. Notifica al usuario.
5. Finaliza el programa cuando Mickey llegue a la salida.

by adra-dev
"""

from os import system
import random

def dibujar_pantalla(matriz):
    system("cls")
    pantalla =""
    total_lineas = 0
    print ("              RESCATE DE MICKY\n")
    print ("         GUIA A MICKY HACIA LA SALIDA\n")
    
    for lineas in matriz:
        total_lineas = total_lineas + 1
    
    for i in range(len(matriz)):
        for o in range(total_lineas):
            pantalla = pantalla + str(matriz [i] [o]) 
        
        print (pantalla)
        pantalla = ""
    print ("\n")
    
def buscar(matriz,que):
    fila = 0
    pantalla = matriz
    caracter = que 
    #queremos obtener la posicion de que(caracter) en la matriz, la fila la obtenemos con fila_result
    #y en cada fila buscamos el caracter que lo escribimos en columna. si tubieramas mas de un caracter 
    #el resultado seria el ultimo
    for i in pantalla:
        try:
            columna = i.index(caracter)
            fila_result = fila
        except:
            pass
        fila = fila + 1
    return fila_result,columna    

def coloca_llave(matriz):
    columna = 0
    fila = len(matriz)
    
    for i in matriz:
        columna = columna +1
        
    while True:
        nueva_fila =  random.randint (0,(fila-1))
        nueva_columna =  random.randint (0,(columna-1))
        print (nueva_fila)
        print (nueva_columna)
        if matriz [nueva_fila] [nueva_columna] ==   "⬜":
           matriz [nueva_fila] [nueva_columna] =   "🔑"
           break       
       
def coloca_micky(matriz):
    columna = 0
    fila = len(matriz)
    
    for i in matriz:
        columna = columna +1
        
    while True:
        nueva_fila =  random.randint (0,(fila-1))
        nueva_columna =  random.randint (0,(columna-1))
        print (nueva_fila)
        print (nueva_columna)
        if matriz [nueva_fila] [nueva_columna] ==   "⬜":
           matriz [nueva_fila] [nueva_columna] =   "🐭"
           break       


"""
pantalla = [ ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","🐭","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],                    
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"],
             ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"], 
             ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],                   
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
             ["🚪","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️"]]
"""
"""
pantalla = [ ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬛️","⬜","⬜","⬜","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️"],
             ["⬛️","⬜","⬛️","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️"],
             ["⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬜","⬜","⬜","⬛️"],
             ["⬛️","⬜","⬜","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬛️","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️"],
             ["⬛️","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬜","⬛️","⬛️","⬜","⬛️"],
             ["⬛️","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬜","⬜","⬛️"],
             ["⬛️","⬛️","⬜","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️"],
             ["⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️"],
             ["⬛️","⬜","⬜","⬛️","⬜","⬜","⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬜","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬜","⬛️","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬜","⬜","⬛️","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬛️","⬛️","⬛️"],
             ["⬛️","⬜","⬛️","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬜","⬜","⬜","⬛️","⬛️","⬛️","⬛️","⬜","⬜","⬜","⬜","⬛️","⬛️"],
             ["⬛️","⬜","⬛️","⬛️","⬜","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬜","⬛️","⬛️"],
             ["⬛️","⬜","⬜","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬛️","⬛️","⬜","⬛️","⬛️"],
             ["⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬛️","⬜","⬛️","⬛️","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬛️","⬛️"],
             ["⬛️","⬛️","⬛️","⬜","⬜","⬜","⬛️","⬜","⬜","⬜","⬛️","⬜","⬛️","⬜","⬛️","⬛️","⬜","⬜","⬜","⬜","⬜","⬛️","⬜","⬛️","⬛️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬜","⬜","⬜","⬛️","⬜","⬜","⬛️","⬛️","⬜","⬜","⬜","⬜","⬛️","⬛️","⬛️","⬜","⬜","⬜","⬛️","⬛️"],
             ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","🚪","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]]
"""

pantalla = [["⬛️","⬛️","⬜","⬛️","🚪","⬛️"],
            ["⬛️","⬛️","⬜","⬛️","⬜","⬛️"],
            ["⬜","⬜","⬜","⬜","⬜","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","⬜","⬛️"]]


salir = 0
llave = False
pasos = 0

coloca_micky(pantalla)
coloca_llave(pantalla)    

while salir == 0:
    
    dibujar_pantalla(pantalla)

    #buscamos a micky y lo retornamos en forma de tuple
    micky = buscar (pantalla,"🐭")
    print (f"MICKY HA ECHO {pasos} PASOS")
    mover = input ("HACIA DONDE IR? \nA-IZQUIERDA D-DERECHA W-ARRIBA S-ABAJO : ").upper()
    
    #obtenemos los valores nuevos de fila y columna segun la opcion que escogemos 
    #colocamos el siguiente caracter en siguiente
    
    if mover == "A":
        siguiente_fila = int(micky[0])
        siguiente_columna = int(micky[1])-1
        
        siguiente = str(pantalla[siguiente_fila] [siguiente_columna])
        
        if siguiente_columna == -1 or siguiente  == "⬛️":  
            print ("HAY UN OBSTACULO.....")
            input ("PULSA ENTER PARA CONTINUAR")
        
        elif siguiente == "🚪" and llave == False:
            print ("LA PUERTA ESTA CERRADA CON LLAVE.....")
            input ("PULSA ENTER PARA CONTINUAR")
            
        elif siguiente == "🚪" and llave == True:
            pantalla [siguiente_fila] [siguiente_columna+1] = "⬜️"
            dibujar_pantalla(pantalla)
            print (F" 🐭 MUY BIEN MICKY ENCUENTRA LA SALIDA !!!!\n    TOTAL DE PASOS: {pasos}")
            p = input ("    QUIERES SALIR ? S - SI N - NO  : ").upper()
            if p == "S":
                salir = 1
            else:
                coloca_micky(pantalla)
                coloca_llave(pantalla)
                llave = False
                pasos = 0
                   
        elif siguiente == "🔑":
                llave = True 
                pantalla [siguiente_fila] [siguiente_columna+1] = "⬜️"
                pantalla [siguiente_fila] [siguiente_columna] = "🐭"
                dibujar_pantalla(pantalla)                        
        
        else:
            pantalla [siguiente_fila] [siguiente_columna+1] = "⬜️"
            pantalla [siguiente_fila] [siguiente_columna] = "🐭"
            dibujar_pantalla(pantalla)
            
    if mover == "D":
        
        siguiente_fila = int(micky[0])
        siguiente_columna = int(micky[1])+1
        
        #el valor de siguiente_columna se pude salir de rango al sumar 1
                
        try:
            siguiente = str(pantalla[siguiente_fila] [siguiente_columna])
        except:
            siguiente = "⬛️"
            
        if siguiente_columna == 24 or siguiente  == "⬛️":
            print ("HAY UN OBSTACULO.....")
            input ("PULSA ENTER PARA CONTINUAR")
            
        elif siguiente == "🚪" and llave == False:
            print ("LA PUERTA ESTA CERRADA CON LLAVE.....")
            input ("PULSA ENTER PARA CONTINUAR")
            
        elif siguiente == "🚪" and llave == True:
            pantalla [siguiente_fila] [siguiente_columna-1] = "⬜️"
            dibujar_pantalla(pantalla)
            print (F" 🐭 MUY BIEN MICKY ENCUENTRA LA SALIDA !!!!\n    TOTAL DE PASOS: {pasos}")
            p = input ("    QUIERES SALIR ? S - SI N - NO  : ").upper()
            if p == "S":
                salir = 1
            else:
                coloca_micky(pantalla)
                coloca_llave(pantalla)
                llave = False
                pasos = 0
                    
        elif siguiente == "🔑":
                llave = True 
                pantalla [siguiente_fila] [siguiente_columna-1] = "⬜️"
                pantalla [siguiente_fila] [siguiente_columna] = "🐭"
                dibujar_pantalla(pantalla)       
        
        else:
            pantalla [siguiente_fila] [siguiente_columna-1] = "⬜️"
            pantalla [siguiente_fila] [siguiente_columna] = "🐭"
            dibujar_pantalla(pantalla)
            
    if mover == "W":

        siguiente_fila = int(micky[0])-1
        siguiente_columna = int(micky[1])
        #el valor de siguiente_columna puede dar -1 pero no da error cuando capturamos siguiente porque comienza al reves
        siguiente = str(pantalla[siguiente_fila] [siguiente_columna])
        
        if siguiente_fila == -1 or siguiente  == "⬛️":
            print (" HAY UN OBSTACULO.....")
            input ("PULSA ENTER PARA CONTINUAR")
            
        elif siguiente == "🚪" and llave == False:
            print ("LA PUERTA ESTA CERRADA CON LLAVE.....")
            input ("PULSA ENTER PARA CONTINUAR")
            
        elif siguiente == "🚪" and llave == True:
            pantalla [siguiente_fila+1] [siguiente_columna] = "⬜️"
            dibujar_pantalla(pantalla)
            print (F" 🐭 MUY BIEN MICKY ENCUENTRA LA SALIDA !!!!\n    TOTAL DE PASOS: {pasos}")
            p = input ("    QUIERES SALIR ? S - SI N - NO  : ").upper()
            if p == "S":
                salir = 1
            else:
                coloca_micky(pantalla)                
                coloca_llave(pantalla)
                llave = False
                pasos = 0
                    
        elif siguiente == "🔑":
                llave = True 
                pantalla [siguiente_fila+1] [siguiente_columna] = "⬜️"
                pantalla [siguiente_fila] [siguiente_columna] = "🐭"
                dibujar_pantalla(pantalla)       
        
        else:
            pantalla [siguiente_fila+1] [siguiente_columna] = "⬜️"
            pantalla [siguiente_fila] [siguiente_columna] = "🐭"
            dibujar_pantalla(pantalla)
            
    if mover == "S":
    
        siguiente_fila = int(micky[0])+1
        siguiente_columna = int(micky[1])
        
        try:
            siguiente = str(pantalla[siguiente_fila] [siguiente_columna])
        except:
            siguiente = "⬛️"
            
        if siguiente_fila == 25 or siguiente  == "⬛️":
            print ("HAY UN OBSTACULO.....")
            input ("PULSA ENTER PARA CONTINUAR")
        
        elif siguiente == "🚪" and llave == False:
            print ("LA PUERTA ESTA CERRADA CON LLAVE.....")
            input ("PULSA ENTER PARA CONTINUAR")
            
        elif siguiente == "🚪" and llave == True:
            pantalla [siguiente_fila-1] [siguiente_columna] = "⬜️"
            dibujar_pantalla(pantalla)
            print (F" 🐭 MUY BIEN MICKY ENCUENTRA LA SALIDA !!!!\n    TOTAL DE PASOS: {pasos}")
            p = input ("    QUIERES SALIR ? S - SI N - NO  : ").upper()
            if p == "S":
                salir = 1
            else:
                coloca_micky(pantalla)
                coloca_llave(pantalla)
                pasos = 0
                llave = False
                    
        elif siguiente == "🔑":
                llave = True 
                pantalla [siguiente_fila-1] [siguiente_columna] = "⬜️"
                pantalla [siguiente_fila] [siguiente_columna] = "🐭"
                dibujar_pantalla(pantalla)       
        
        else:
            pantalla [siguiente_fila-1] [siguiente_columna] = "⬜️"
            pantalla [siguiente_fila] [siguiente_columna] = "🐭"
            dibujar_pantalla(pantalla)
    
    pasos = pasos +1