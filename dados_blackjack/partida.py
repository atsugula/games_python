from jugador import Jugador
import random
import menu
# Section de variables globales
cant_jugadores=0
apuesta_general=5000
total_apuesta=0
jugadores=[] # Variable que guarda la lista de jugadores
colores=[31,32,33,34,35,36,37]
# Generamos colores por cada jugador
def generarColor():
    color=random.randrange(7)
    return color
# Mostramos todos los datos de los jugadores
def mostrarTodo():
    datos=""
    menu.barra()
    for i in range(0,cant_jugadores+1):
        datos+=f"""\033[1;{jugadores[i].color}m
        ==============| LOS DATOS DEL JUGADOR {i} |==============
        NOMBRE DEL JUGADOR      : {jugadores[i].nombre}
        MONTO INICIAL           : {jugadores[i].dinero_inicia}
        SUMA DE PUNTOS          : {jugadores[i].suma_tiros}
        PARTIDAS DE PERDIDAS    : {jugadores[i].perdidas}
        TOTAL TIROS             : {jugadores[i].total_tiros}
        NUMERO DE TIROS         : {jugadores[i].total_tiros}
        NUMERO DE TIROS (1)     : {jugadores[i].tiros_uno}
        TURNO                   : {jugadores[i].turno}
        PLANTADO                : {jugadores[i].planto}
        """
    print(datos)
    input()
    menu.limpiar()
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

# Determinamos cuantos van a jugar esta pártida
def cuantosJugadores():
    global cant_jugadores, apuesta_general
    while True:
        try:
            cant_jugadores=int(input('¿Cuántos personas van a jugar? -> '))
            apuesta=int(input('¿Con cuánto van a jugar? (Ingrese 0 si quieren dejarla por defecto) -> '))
            if (apuesta!=0):
                if (apuesta>=500):
                    apuesta_general=apuesta
                else:
                    raise ValueError(menu.mensaje_monto())
            break
        except ValueError:
            menu.mensaje_error()
    menu.limpiar()
# Le ponemos los datos por defecto a la casa
def iniciarCasa():
    # Se sigue el orden segun nuestra clase
    dado=0
    color=35
    turno=False
    nombre='Casa'
    planto=False
    tiros_uno=0
    suma_tiros=0
    total_tiros=0
    perdidas=0
    dinero_inicia=apuesta_general
    # Creamos nuestro clase y le pasamos los datos
    nuevo_jugador=Jugador(dado, color, turno, nombre, planto, perdidas, tiros_uno, suma_tiros, total_tiros, dinero_inicia)
    # Agregamos el nuevo jugador a nuestra lista
    jugadores.append(nuevo_jugador)
# Pedimos los datos de todas las personas e inicializamos todo por defecto
def pedirJugadores():
    for i in range(0, cant_jugadores):
        # Se sigue el orden segun nuestra clase
        dado=0
        color=colores[generarColor()]
        turno=False
        nombre=input('Ingrese el nombre del jugador: ')
        planto=False
        tiros_uno=0
        suma_tiros=0
        total_tiros=0
        perdidas=0
        dinero_inicia=apuesta_general
        # Creamos nuestro clase y le pasamos los datos
        nuevo_jugador=Jugador(dado, color, turno, nombre, planto, perdidas, tiros_uno, suma_tiros, total_tiros, dinero_inicia)
        # Agregamos el nuevo jugador a nuestra lista
        jugadores.append(nuevo_jugador)
        menu.limpiar()
# metodo principal del juego
def main():
    cuantosJugadores()
    iniciarCasa()
    pedirJugadores()
    mostrarTodo()