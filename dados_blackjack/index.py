# Menu principal del juego
import menu
# Metodo principal
while True:
    print("""
    =========================| BLACKJACK DADOS |=========================
        
        Objetivo: Superar a la Casa para pasar los 21 puntos.

        (1) VER REGLAS
        (2) VER LIMITES
        (3) EMPEZAR A JUGAR
        (4) LIMPIAR CONSOLA
        (5) SALIR DEL JUEGO

    """)
    # Si digita alguna letra le traiga un mensaje y siga con el menu
    try:
        decision=int(input('Ingrese la opción que desea: '))
        # Ejecutamos la decision que haya elegido
        if (decision==1):
            menu.reglas()
        elif (decision==2):
            menu.limites()
        elif (decision==3):
            menu.empezar()
        elif (decision==4):
            menu.limpiar()
        elif (decision==5):
            break
        else:
            print('Ups!!! Ingreso una opción no válida, por favor lea')
    except ValueError:
        menu.mensaje_error()