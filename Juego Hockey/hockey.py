from os import system
import keyboard,time,random,pygame
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.mixer.init()

def mostrar_pantalla(matriz,uno,dos,t_1,t_2):
    system("cls")
    print (f" MARCADOR.  {uno} - {dos}\n")
    print(f"TIEMPO 1 ENR: {t_1}")
    print(f"ENERGIA {"".join(energia1)}\n")
    print ("     PLAYER 1")
    for i in matriz:
        print("".join(i))
    print ("     PLAYER 2\n")
    print(f"ENERGIA {"".join(energia2)}")
    print(f"TIEMPO 2 ENR: {t_2}\n")

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(100)
efecto_1 = pygame.mixer.Sound('Golpe.mp3')
efecto_2 = pygame.mixer.Sound('Bocina.mp3')

salir = 0
marcador1=0
marcador2=0

# Saque inicial aleatoria 
com_j1=0
com_j2=0
com= random.randint(1,2)
if com == 1:
    com_j1=1
else:
    com_j2=1

while salir == 0:
    pygame.mixer.music.set_volume(0.9)# atenuo la musica de fondo
    pantalla = [["┌","🟥","🟥","🟥","🟥","🟥","🟥","🟥"," ┐"],
                ["│","🟦​","🟦​","🟦​","🔶​​","🟦​","🟦​","🟦​"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","⚫","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦","🟦","🟦","🟦","🟦","🟦","🟦"," │"],
                ["│","🟦​","🟦​","🟦​","🥌​","🟦​","🟦​","🟦​"," │"],
                ["└","🟥","🟥","🟥","🟥","🟥","🟥","🟥"," ┘"]
                ]
    
    energia1 = ["🟦","🟦","🟦","🟦","🟦"]
    energia2 = ["🟦","🟦","🟦","🟦","🟦"]
    numero1 = 1
    numero2 = 1
    energia_player1 = 1
    energia_player2 = 1
    mueve_disco = 5
    fila_disco=6
    columna_disco=4
    disco_movimiento=0
    disco = "⚫"
    raqueta_1 = "🔶​​"
    fila_pl1 = 0
    fila_playeruno = 0
    columna_playeruno = 0
    raqueta_2 = "🥌​"

    fila = 0
    tiempo1=0
    tiempo2=0

    mostrar_pantalla(pantalla,marcador1,marcador2,tiempo1,tiempo2)
    
    # Compruebo quien hace el saque
    if com_j1==1:
        print ("  SACA JUGADOR 1")
        time.sleep(5)
        # Animacion del jugador 1 para sacar
        for i in range(1,5):
            pantalla[i][4]="🟦" 
            pantalla[i+1][4]="🔶​​"
            mostrar_pantalla(pantalla,marcador1,marcador2,tiempo1,tiempo2)
            time.sleep(0.3)
        disco_movimiento=random.randint(1,3)
        com_j1=0

    elif com_j2==1:
        print ("  SACA JUGADOR 2")
        time.sleep(5)
        com_j2=0    

    salir = input ("COMIEZA EL PARTIDO..\n  (PULSA ENTER)\n     (SALIR)\n      ").lower()
    
    if salir == "salir":
        salir = 1
        system("cls")
        break
    else:
        salir=0

    while True:
        
        fila = 0
        fila_dis = 0
        fila_pl = 0

        mostrar_pantalla(pantalla,marcador1,marcador2,tiempo1,tiempo2)
        pygame.mixer.music.set_volume(0.5)# atenuo la musica de fondo

        #Localizar raqueta1 con fila_playeruno y columna_playeruno
        for i in pantalla:
            try:
                columna_playeruno = i.index(raqueta_1)
                fila_playeruno = fila_pl
            except:
                pass
            fila_pl = fila_pl + 1
        
        #Localizar raqueta2 con fila_raqueta2 y columna 
        for i in pantalla:
            try:
                columna = i.index(raqueta_2)    
                fila_raqueta2 = fila           
            except:
                pass
            fila = fila + 1
        
        #Localizar disco con fila_disco y columna_disco
        for i in pantalla:
            try:
                columna_disco = i.index(disco)    
                fila_disco = fila_dis           
            except:
                pass
            fila_dis = fila_dis + 1
        
        time.sleep(0.08)
        # Segun la cantidad de bucles que va haciendo se aumenta el tiempo para contolar la energia
        tiempo1 +=2
        tiempo2 +=2
        
        if tiempo1 < 999:
            energia_player1=1
            energia_player2=1
        if tiempo1  >= 1000:
            energia_player1=2
            energia1[4]="🟥"
        if tiempo1 >= 2000:
            energia_player1=3
            energia1[3]="🟥"
        if tiempo1 >= 3000:
            energia_player1=4
            energia1[2]="🟥"
        if tiempo1 >= 4000:
            energia_player1=5
            energia1[1]="🟥"

        if numero1 == energia_player1:    
            numero1=0

            # Movimiento player 1    
            if fila_playeruno>1:
                fila_playeruno=fila_playeruno-1
                pantalla[fila_playeruno+1][columna_playeruno]="🟦" 
                pantalla[fila_playeruno][columna_playeruno]="🔶​​"

            if columna_disco > columna_playeruno:
                if pantalla[fila_playeruno+1][columna_playeruno]=="⚫":
                    efecto_1.play()
                    aleatorio = random.randint(1,3)
                    disco_movimiento=aleatorio
                    
                else:
                    pantalla[fila_playeruno][columna_playeruno]="🟦" 
                    pantalla[fila_playeruno][columna_playeruno+1]="🔶​​"
                    tiempo1+=5

            if columna_disco < columna_playeruno:
                if pantalla[fila_playeruno+1][columna_playeruno]=="⚫":
                    efecto_1.play()
                    aleatorio = random.randint(1,3)
                    disco_movimiento=aleatorio
                    
                else:
                    pantalla[fila_playeruno][columna_playeruno]="🟦" 
                    pantalla[fila_playeruno][columna_playeruno-1]="🔶​​"
                    tiempo1+=5

            if columna_disco == columna_playeruno and pantalla[fila_playeruno+1][columna_playeruno]=="⚫":
                efecto_1.play()
                aleatorio = random.randint(1,3)
                disco_movimiento=aleatorio
                tiempo1-=10

        numero1+=1

        # Movimintos del disco cada 5 bucles del while
        if mueve_disco==5:
            mueve_disco = 0
            # Movimiento rectos de disco
            if disco_movimiento==8:
                pantalla[fila_disco-1][columna_disco]="⚫"
                pantalla[fila_disco][columna_disco]="🟦"
                            
            elif disco_movimiento==2:
                if fila_disco+1<13:
                    if  pantalla[fila_disco+1][columna_disco]=="🥌​":
                        efecto_1.play()
                        aleatorio=random.randint(7,9)
                        disco_movimiento=aleatorio
                    else:    
                        pantalla[fila_disco+1][columna_disco]="⚫"
                        pantalla[fila_disco][columna_disco]="🟦"
                        
                else:
                    efecto_2.play()
                    marcador1+=1
                    com_j2=1
                    print (" HAN MARCADO GOL\n   AL PLAYER 2\n")
                    input(f"  (PULSA ENTER)\n")
                    break
            elif disco_movimiento==4:
                if pantalla[fila_disco][columna_disco-1] == "│":
                    efecto_1.play()
                    
                    disco_movimiento=9
                else:    
                    pantalla[fila_disco][columna_disco-1]="⚫"
                    pantalla[fila_disco][columna_disco]="🟦"
            
            elif disco_movimiento==6:
                if pantalla[fila_disco][columna_disco+1] == " │":    
                    efecto_1.play()
                    
                    disco_movimiento=1
                else:
                    pantalla[fila_disco][columna_disco+1]="⚫"
                    pantalla[fila_disco][columna_disco]="🟦"

            # Movimientos inclinados de disco
            elif disco_movimiento==9:
                if fila_disco>0:    
                    if pantalla[fila_disco][columna_disco+1] == " │" or pantalla[fila_disco][columna_disco+1] == " ┐":
                        efecto_1.play()
                        disco_movimiento=7
                    else:
                        pantalla[fila_disco-1][columna_disco+1]="⚫"
                        pantalla[fila_disco][columna_disco]="🟦"
                else:
                    efecto_2.play()
                    marcador2+=1
                    com_j1=1
                    print (" HAN MARCADO GOL\n   AL PLAYER 1\n")
                    input(f"  (PULSA ENTER)\n")
                    break
            
            elif disco_movimiento==7:
                if fila_disco>0:
                    if pantalla[fila_disco][columna_disco-1] == "│" or pantalla[fila_disco][columna_disco-1] == "┌":
                        efecto_1.play()
                        disco_movimiento=9
                    else:    
                        pantalla[fila_disco-1][columna_disco-1]="⚫"
                        pantalla[fila_disco][columna_disco]="🟦"
                else:
                    efecto_2.play()
                    marcador2+=1
                    com_j1=1
                    print (" HAN MARCADO GOL\n   AL PLAYER 1\n")
                    input(f"  (PULSA ENTER)\n")
                    break
            
            elif disco_movimiento==3:
                if fila_disco<12:
                    if pantalla[fila_disco+1][columna_disco+1] == " │" or pantalla[fila_disco+1][columna_disco+1] == " ┘":
                        efecto_1.play()
                        disco_movimiento=1
                    elif pantalla[fila_disco+1][columna_disco+1] == "🥌​":
                        efecto_1.play()
                        disco_movimiento=7    
                    else:    
                        pantalla[fila_disco+1][columna_disco+1]="⚫"
                        pantalla[fila_disco][columna_disco]="🟦"
                else:
                    efecto_2.play()
                    marcador1+=1
                    com_j2=1
                    print (" HAN MARCADO GOL\n   AL PLAYER 2\n")
                    input(f"  (PULSA ENTER)\n")
                    break

            elif disco_movimiento==1:
                if fila_disco<12:
                    if pantalla[fila_disco][columna_disco-1] == "│" or pantalla[fila_disco][columna_disco-1] == "└":
                        efecto_1.play()
                        disco_movimiento=3
                    elif pantalla[fila_disco+1][columna_disco-1] == "🥌​":
                        efecto_1.play()
                        disco_movimiento=9    
                    else:
                        pantalla[fila_disco+1][columna_disco-1]="⚫"
                        pantalla[fila_disco][columna_disco]="🟦"
                else:
                    efecto_2.play()
                    
                    marcador1+=1
                    com_j2=1
                    
                    print (" HAN MARCADO GOL\n   AL PLAYER 2\n")
                    input(f"  (PULSA ENTER)\n")
                    break

        mueve_disco+=1    
        
        if tiempo2 < 999:
            energia_player2=1
        if tiempo2  >= 1000:
            energia_player2=2
            energia2[4]="🟥"
        if tiempo2 >= 2000:
            energia_player2=3
            energia2[3]="🟥"
        if tiempo2 >= 3000:
            energia_player2=4
            energia2[2]="🟥"
        if tiempo2 >= 4000:
            energia_player2=5
            energia2[1]="🟥"

        if numero2 == energia_player2:    
            numero2=0
            # Movimientos rectos de raqueta2
            
            if keyboard.is_pressed("8"):
                if fila_raqueta2>1:
                    if pantalla[fila_raqueta2-1][columna] == "⚫":
                        efecto_1.play()
                        disco_movimiento=8    
                    else:          
                        pantalla[fila_raqueta2 -1 ][columna] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"

            if keyboard.is_pressed("2"):
                if fila_raqueta2<11:
                    if pantalla[fila_raqueta2+1][columna] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=2
                    else:          
                        pantalla[fila_raqueta2 +1][columna] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"

            if keyboard.is_pressed("4"):
                if columna>1:
                    if pantalla[fila_raqueta2][columna-1] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=4
                    else:          
                        pantalla[fila_raqueta2][columna-1] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"
            
            if keyboard.is_pressed("6"):
                if columna < 7:
                    if pantalla[fila_raqueta2][columna+1] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=6
                    else:                    
                        pantalla[fila_raqueta2][columna+1] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"
            
            #Movimientos inclinados de raqueta2
            if keyboard.is_pressed("9"):
                if fila_raqueta2>1 and columna<7:
                    if pantalla[fila_raqueta2-1][columna+1] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=9
                    else:        
                        pantalla[fila_raqueta2-1][columna+1] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"
                        tiempo2+=10      

            if keyboard.is_pressed("7"):
                if fila_raqueta2>1 and columna>1:
                    if pantalla[fila_raqueta2-1][columna-1] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=7
                    else:        
                        pantalla[fila_raqueta2-1][columna-1] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"
                        tiempo2+=10

            if keyboard.is_pressed("3"):
                if fila_raqueta2<11 and columna<7:    
                    if pantalla[fila_raqueta2+1][columna+1] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=3
                    else:        
                        pantalla[fila_raqueta2+1][columna+1] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"  
                        tiempo2+=10

            if keyboard.is_pressed("1"):
                if fila_raqueta2<11 and columna>1:
                    if pantalla[fila_raqueta2+1][columna-1] == "⚫":
                        efecto_1.play()
                        
                        disco_movimiento=1
                    else:        
                        pantalla[fila_raqueta2+1][columna-1] = "🥌​"
                        pantalla[fila_raqueta2][columna] = "🟦​"
                        tiempo2+=10

        numero2+=1
    
