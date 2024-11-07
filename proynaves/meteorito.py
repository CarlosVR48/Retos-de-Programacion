from os import system
import time,random,keyboard,pygame

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.mixer.init()

global pos_nave,puntos,velocidad 
p_0 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_1 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_2 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_3 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_4 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_5 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_6 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_7 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_8 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
p_9 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
pos_nave = 5
puntos = 0
estado = False
salir = "continuar"

def pintar_pantalla():
    global puntos
    izquierda = "  |"
    derecha = "|"
    system("cls")
    print ("        DESTRULLE LOS METEORITOS")
    print ("     Y QUE NO SOBREPASEN TU LINEA")
    print ("     O - IZQ , P - DER , D - DISP")
    print (izquierda,str(p_0[0]),str(p_0[1]),str(p_0[2]),str(p_0[3]),str(p_0[4])
               ,str(p_0[5]),str(p_0[6]),str(p_0[7]),str(p_0[8]),str(p_0[9]),derecha)
    print (izquierda,str(p_1[0]),str(p_1[1]),str(p_1[2]),str(p_1[3]),str(p_1[4])
               ,str(p_1[5]),str(p_1[6]),str(p_1[7]),str(p_1[8]),str(p_1[9]),derecha)
    print (izquierda,str(p_2[0]),str(p_2[1]),str(p_2[2]),str(p_2[3]),str(p_2[4])
               ,str(p_2[5]),str(p_2[6]),str(p_2[7]),str(p_2[8]),str(p_2[9]),derecha)
    print (izquierda,str(p_3[0]),str(p_3[1]),str(p_3[2]),str(p_3[3]),str(p_3[4])
               ,str(p_3[5]),str(p_3[6]),str(p_3[7]),str(p_3[8]),str(p_3[9]),derecha)
    print (izquierda,str(p_4[0]),str(p_4[1]),str(p_4[2]),str(p_4[3]),str(p_4[4])
               ,str(p_4[5]),str(p_4[6]),str(p_4[7]),str(p_4[8]),str(p_4[9]),derecha)
    print (izquierda,str(p_5[0]),str(p_5[1]),str(p_5[2]),str(p_5[3]),str(p_5[4])
               ,str(p_5[5]),str(p_5[6]),str(p_5[7]),str(p_5[8]),str(p_5[9]),derecha)
    print (izquierda,str(p_6[0]),str(p_6[1]),str(p_6[2]),str(p_6[3]),str(p_6[4])
               ,str(p_6[5]),str(p_6[6]),str(p_6[7]),str(p_6[8]),str(p_6[9]),derecha)
    print (izquierda,str(p_7[0]),str(p_7[1]),str(p_7[2]),str(p_7[3]),str(p_7[4])
               ,str(p_7[5]),str(p_7[6]),str(p_7[7]),str(p_7[8]),str(p_7[9]),derecha)
    print (izquierda,str(p_8[0]),str(p_8[1]),str(p_8[2]),str(p_8[3]),str(p_8[4])
               ,str(p_8[5]),str(p_8[6]),str(p_8[7]),str(p_8[8]),str(p_8[9]),derecha)
    print (izquierda,str(p_9[0]),str(p_9[1]),str(p_9[2]),str(p_9[3]),str(p_9[4])
               ,str(p_9[5]),str(p_9[6]),str(p_9[7]),str(p_9[8]),str(p_9[9]),derecha)
    print (f"\n         TUS PUNTOS SON: {puntos}")
 
def mov_meteor(pos_asteroides):
    global pos_nave,puntos,velocidad 
    i = 0
    posicion =int(pos_asteroide)
    
    if puntos == 0:
        velocidad = 0.4
    elif puntos > 100:
        velocidad = 0.3
    elif puntos > 200:
        velocidad = 0.2  
    elif puntos > 300:
        velocidad = 0.1  
    elif puntos > 400:
        velocidad = 0.005  

    while i <10:
        
        if keyboard.is_pressed("o") and not(pos_nave==0):
            p_9[pos_nave] = "⬛"
            pintar_pantalla()
            pos_nave = pos_nave-1
            p_9[pos_nave] = "🚀"
        if keyboard.is_pressed("p") and not(pos_nave==9):
            p_9[pos_nave] = "⬛"
            pintar_pantalla()
            pos_nave = pos_nave+1
            p_9[pos_nave] = "🚀"
        if keyboard.is_pressed("d"):
            efecto_1.play()
            p_8[pos_nave] = "💣"
            pintar_pantalla()

        if i == 0 and p_0[posicion] == "⬛":
            p_0[posicion] ="☄️ "
        elif i ==1:
            if p_1[posicion] == "⬛":
                p_0[posicion] = "⬛"
                p_1[posicion] = "☄️ "
        elif i ==2:
            if p_2[posicion] == "⬛":
                p_1[posicion] = "⬛"
                p_2[posicion] = "☄️ "
        elif i ==3:
            if p_3[posicion] == "⬛":
                p_2[posicion] = "⬛"
                p_3[posicion] = "☄️ "
        elif i ==4:
            if p_4[posicion] == "⬛":
                p_3[posicion] = "⬛"
                p_4[posicion] = "☄️ "
        elif i ==5:
            if p_5[posicion] == "⬛":
                p_4[posicion] = "⬛"
                p_5[posicion] = "☄️ "
        elif i ==6:
            if p_6[posicion] == "⬛":
                p_5[posicion] = "⬛"
                p_6[posicion] = "☄️ "
        elif i ==7:
            if p_7[posicion] == "⬛":
                p_6[posicion] = "⬛"
                p_7[posicion] = "☄️ "
        elif i ==8:
            if p_8[posicion] == "💣":
                efecto_2.play()
                p_7[posicion] = "⬛"
                p_8[posicion] = "⬛"
                puntos = puntos + 10
                i=10
            elif p_8[posicion] == "⬛":
                p_7[posicion] = "⬛"
                p_8[posicion] = "☄️ "
        elif i ==9:
            if p_9[posicion] == "⬛" or p_9[posicion] == "🚀":
                efecto_3.play()
                p_8[posicion] = "⬛"
                p_9[posicion] = "☄️ "
                pintar_pantalla()
                return True
        
        i = i + 1
        pintar_pantalla()       
        time.sleep((velocidad))

def pregunta ():
    while True:
        if keyboard.is_pressed("n"):
            return "n"
        if keyboard.is_pressed("s"):
            return "s"
        if keyboard.is_pressed("space"):
            return ""

pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(7)
efecto_1 = pygame.mixer.Sound('explosion.wav')
efecto_2 = pygame.mixer.Sound('alarma.wav')
efecto_3 = pygame.mixer.Sound('01.wav')

p_9[int(pos_nave)] = "🚀"  
pintar_pantalla()
print ("    PULSA ESPACIO PARA COMENZAR")
pregunta()
 
while salir == "continuar":
    pos_asteroide =  random.randint (0, 9)
    estado = mov_meteor(pos_asteroide)
    
    if estado == True :
        print ("    EL METEORITO SOBREPASO TU ZONA")
        time.sleep (2)
        print("       QUIERES REINTENTAR? S/N  ")
        while True:
            salir = pregunta()

            if  salir == "n":
                salir = "salir"
                break
            elif salir == "s":
                p_8 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
                p_9[pos_asteroide] = "⬛"
                p_9[pos_nave] = "🚀"
                puntos = 0
                pintar_pantalla()
                salir = "continuar"
                break
            else: 
                pass

pygame.mixer.music.stop()    