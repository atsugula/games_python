import os
import sys
import time
import partida
from tqdm import tqdm
# Detectamos que sistema operativo tiene nuestro PC
def sistema(comando1, comando2): # En base a eso, ejecutamos el respectivo comando
    if os.name == "nt":
        os.system(comando1)
    else:
        os.system(comando2)
# Funcion para limpiar pantalla dependiendo del sistema operativo
def limpiar():
    sistema('cls', 'clear')

def mensaje_ganador(nombre,plata): # Mensaje de final de la partida
    limpiar()
    print(f"""\033[1;37m
        =========================| BLACKJACK DADOS |=========================
                ¡¡¡FELICIDADES {nombre} ACABAS DE GANAR LA RONDA!!!
                ¡USTED GANA ${plata} QUE SE LE SUMARON A SU CUENTA!""")
    input()
    limpiar()
def reglas():
    limpiar()
    print("""\033[1;37m
    ===================================| BLACKJACK REGLAS |===================================

        * Se reparten dos dados por jugador.

        * Al inicio todos tiran un dado y el que saque mayor, comienza sacando, 
            los otros jugadores siguen en orden descendiente.

        * Si el jugador quiere aumentar su puntaje puede lanzar nuevamente los dados. 

        * Los puntos obtenidos en cada lanzamiento se suma al puntaje anterior.

        * Si su puntaje es igual a 1, automaticamente pierde.

        * Cuando un jugador tiene 15 o más puntos, puede lanzar 1 dado si quiere 
            aumentar su puntaje.

        * El jugador puede plantarse en cualquier momento, si no ha superado los 21 puntos.

        * Cuando un jugador se planta o supera los 21 puntos termina su turno.

        * La Casa lanza sus dados luego que todos los jugadores han jugado. 
            Lanza nuevamente si tiene 16 o menos puntos y se planta con 17 o más puntos.

        * Gana el jugador que supera la Casa sin pasarse de los 21 puntos.

        * Si todos se rinden o se pasan, la casa gana.

        * Si la casa se pasa, gana el jugador con el puntaje más alto, sin pasarse de 21.

        * Una vez empieza la partida, no para hasta que haya un ganador.
    """)
    input()
    limpiar()

def limites():
    limpiar()
    print("""\033[1;37m
    ===================================| BLACKJACK LIMITES |===================================

        * Hay un maximo de 8 jugadores por partida.

        * No existe el limite de tiempo por partida.
        
        * Todos los jugadores empiezan con 5000 o apuesta acordada entre todos.

        * Lo mínimo para empezar la partida es de 500.
    """)
    input()
    limpiar()

def empezar():
    limpiar()
    partida.main()

def mensaje_error():
    limpiar()
    print("""\033[1;31m
        Ups!!! Ingreso una opción no válida, por favor ingrese solo números
        ------------- Presione cualquier tecla para continuar -------------""")
    input()
    limpiar()

def mensaje_dado(nombre):
    limpiar()
    print(f"""\033[1;36m
                            JUGADOR {nombre}
            Está apunto de tirar, respire y buena suerte!!!
        ------ Presione cualquier tecla para continuar ------""")
    input()
    limpiar()

def mensaje_monto():
    limpiar()
    print("""\033[1;31m
        Ups!!! Ingreso una opción no válida, ingrese un número mayor a 500
        ------------- Presione cualquier tecla para continuar -------------""")
    input()
    limpiar()

def juegoPerdido(nombre):
    limpiar()
    print(f"""\033[1;31m
        Ups!!! El jugador {nombre} acaba de perder, queda por fuera de la ronda
        --------------- Presione cualquier tecla para continuar ---------------""")
    input()
    limpiar()

# Una barra de progreso
def barra():
    limpiar()
    print('\033[1;32m')
    for i in tqdm(range(100)):
        time.sleep(0.01)
    limpiar()

# Borrar cache
def limpiarCache():
    sistema('rmdir /s __pycache__', 'rm -r __pycache__')
    
# Pintamos el logo
def logo():
    print(f"""\033[1;35m
                           .------------------.
                         ./                    \.
                        ./   \.    ./\.    ./   \.
                       .|     \.  ./  \.  ./     |.
                       .|      \../    \../      |.
                       .|       \. ATSU ./       |.
                       .|      ./\.    ./\.      |.
                       .|     ./  \.  ./  \.     |.
                        .\   ./    \../    \.   /.
                         .\                    /.
                           .------------------.""")