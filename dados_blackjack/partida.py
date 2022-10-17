import random
import menu
from jugador import Jugador
""" 
    Section de variables globales
"""
cant_jugadores=0
apuesta_general=5000
jugadores=[] # Variable que guarda la lista de jugadores

# Mostramos los dados por cada tiro del jugador
def pintarDados(d1,d2):
    if (d2==0): # Para cuando se requiera solo pintar uno
        print(f"""
        :::::::::
        ::     ::
        ::  {d1}  ::
        ::     ::
        :::::::::
        """)
    else: # Los dos dados por defecto del juego
        print(f"""
        :::::::::   :::::::::
        ::     ::   ::     ::
        ::  {d1}  ::   ::  {d2}  ::
        ::     ::   ::     ::
        :::::::::   :::::::::
        """)
# Genera un solo numero aleatorio
def generarTiro():
    tiro=random.randrange(6)+1
    return tiro

""" def nose(x):
    if x>0:
        print(generarTiro())
        return nose(x-1)
    return x
x=nose(2) """
# Determinamos cuantos van a jugar esta pártida
def cuantosJugadores():
    global cant_jugadores, apuesta_general
    while True:
        try:
            cant_jugadores=int(input('¿Cuántos personas van a jugar? -> '))
            apuesta=int(input('¿Con cuánto van a jugar? (Ingrese 0 si quieren dejarla por defecto) -> '))
            if (apuesta!=0):
                apuesta_general=apuesta
            break
        except ValueError:
            menu.mensaje_error()
# Le ponemos los datos por defecto a la casa
def iniciarCasa():
    # Se sigue el orden segun nuestra clase
    dado=0
    turno=False
    nombre='Casa'
    planto=False
    tiros_uno=0
    suma_tiros=0
    total_tiros=0
    dinero_inicia=apuesta_general
    # Creamos nuestro clase y le pasamos los datos
    nuevo_jugador=Jugador(dado, turno, nombre, planto, tiros_uno, suma_tiros, total_tiros, dinero_inicia)
    # Agregamos el nuevo jugador a nuestra lista
    jugadores.append(nuevo_jugador)
# Pedimos los datos de todas las personas e inicializamos todo por defecto
def pedirJugadores():
    for i in range(0, cant_jugadores):
        # Se sigue el orden segun nuestra clase
        dado=0
        turno=False
        nombre=input('Ingrese el nombre del jugador: ')
        planto=False
        tiros_uno=0
        suma_tiros=0
        total_tiros=0
        dinero_inicia=apuesta_general
        # Creamos nuestro clase y le pasamos los datos
        nuevo_jugador=Jugador(dado, turno, nombre, planto, tiros_uno, suma_tiros, total_tiros, dinero_inicia)
        # Agregamos el nuevo jugador a nuestra lista
        jugadores.append(nuevo_jugador)
# metodo principal del juego
def main():
    cuantosJugadores()
    iniciarCasa()
    pedirJugadores()
    input()
