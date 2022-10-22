from matplotlib.pyplot import bar_label
from jugador import Jugador
import random
import menu
# Section de variables globales
cant_jugadores=0
apuesta_jugador=5000
total_apuesta=0
jugadores=[] # Variable que guarda la lista de jugadores
colores=[31,32,33,34,35,36,37]
# Generamos colores por cada jugador
def generarColor():
    color=random.randrange(6)
    return color
# Mostramos todos los datos de los jugadores
def mostrarTodo():
    datos=""
    menu.barra()
    for i, juga in enumerate(jugadores):
        datos+=f"""\033[1;{juga.color}m
        ==============| LOS DATOS DEL JUGADOR {i} |==============
        NOMBRE DEL JUGADOR      : {juga.nombre}
        ULTIMO DADO DEL JUGADOR : {juga.dado}
        NUMERO DE TIROS (1)     : {juga.tiros_uno}
        NUMERO DE TIROS         : {juga.total_tiros}
        SUMA DE PUNTOS          : {juga.suma_dados}
        MONTO INICIAL           : {juga.dinero_inicia}
        TOTAL TIROS             : {juga.total_tiros}
        TURNO                   : {juga.turno}
        PLANTADO                : {juga.planto}
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
    input()
    menu.limpiar()
# Genera un solo numero aleatorio
def generarTiro():
    tiro=random.randrange(6)+1
    return tiro
# Determinamos cuantos van a jugar esta pártida
def cuantosJugadores():
    global cant_jugadores, apuesta_jugador
    while True:
        try:
            print('\033[1;37m')
            cant_jugadores=int(input('¿Cuántos personas van a jugar? -> '))
            apuesta=int(input('¿Con cuánto van a jugar? (Ingrese 0 si quieren dejarla por defecto) -> '))
            if (apuesta!=0):
                if (apuesta>=500):
                    apuesta_jugador=apuesta
                else:
                    raise ValueError(menu.mensaje_monto())
            break
        except ValueError:
            menu.mensaje_error()
    menu.limpiar()
# Le ponemos los datos por defecto a la casa
def iniciarCasa():
    global total_apuesta
    # Se sigue el orden segun nuestra clase
    dado=0
    gana=0
    color=35
    turno=False
    nombre='Casa'
    planto=False
    tiros_uno=0
    suma_dados=0
    total_tiros=0
    perdio=0
    dinero_inicia=apuesta_jugador
    # Creamos nuestro clase y le pasamos los datos
    nuevo_jugador=Jugador(dado, gana, color, turno, nombre, planto, perdio, tiros_uno, suma_dados, total_tiros, dinero_inicia)
    # Agregamos el nuevo jugador a nuestra lista
    jugadores.append(nuevo_jugador)
    # Sumamos la apuesta base
    total_apuesta+=500
# Pedimos los datos de todas las personas e inicializamos todo por defecto
def pedirJugadores():
    global total_apuesta
    for i in range(0, cant_jugadores):
        # Se sigue el orden segun nuestra clase
        dado=0
        gana=0
        color=colores[generarColor()]
        turno=False
        nombre=input('Ingrese el nombre del jugador: ')
        planto=False
        tiros_uno=0
        suma_dados=0
        total_tiros=0
        perdio=0
        dinero_inicia=apuesta_jugador
        # Creamos nuestro clase y le pasamos los datos
        nuevo_jugador=Jugador(dado, gana, color, turno, nombre, planto, perdio, tiros_uno, suma_dados, total_tiros, dinero_inicia)
        # Agregamos el nuevo jugador a nuestra lista
        jugadores.append(nuevo_jugador)
        # Sumamos la apuesta base
        total_apuesta+=500
        menu.limpiar()
# Pasar turno
def pasarTurno(i):
    jugadores[i].turno=False
    if(i==len(jugadores)-1):
        jugadores[0].turno=True
    else:
        jugadores[i+1].turno=True
# Tirar los dados para un jugador
def lanzarDados(i):
    salir=0
    while salir==0:
        d1=generarTiro()
        d2=generarTiro()
        if (jugadores[i].suma_dados!=0):
            if (jugadores[i].suma_dados>=21):
                menu.juegoPerdido(jugadores[i].nombre)
                jugadores[i].perdio=1
                break
            else:
                try:
                    salir=int(input(f'¿Quiere plantarse con {jugadores[i].suma_dados} puntos? Si(1) No(0) '))
                except ValueError:
                    menu.mensaje_error()
                if (salir==1): break
                if (jugadores[i].suma_dados>=15):
                    menu.limpiar()
                    quiere=input('¿Desea tirar un solo dado? Si(s) No(n) ')
                    if (quiere=="s" or quiere=="S"):
                        menu.mensaje_dado(jugadores[i].nombre)
                        pintarDados(d1,0)
                        jugadores[i].suma_dados+=d1
                        menu.limpiar()
                else:
                    menu.mensaje_dado(jugadores[i].nombre)
                    pintarDados(d1,d2)
                    jugadores[i].suma_dados+=(d1+d2)
                    menu.limpiar()
        else:
            menu.mensaje_dado(jugadores[i].nombre)
            pintarDados(d1,d2)
            jugadores[i].suma_dados+=(d1+d2)
            menu.limpiar()
    if (jugadores[i].perdio!=1):
        jugadores[i].planto=True
        pasarTurno(i)
    else:
        pasarTurno(i)
        jugadores.remove(jugadores[i])
    mostrarTodo()

# Inicio del juego, datos por defecto
def inicio():
    cuantosJugadores()
    iniciarCasa()
    pedirJugadores()
    mostrarTodo()
# Proceso que se repite hasta que haya un ganador
def jugar(i):
    ganador=False
    while not ganador:
        lanzarDados(i)
        ganador=validarGanador(i)
        i+=1
    mostrarTodo()
    menu.mensaje_ganador(jugadores[i-1].nombre,total_apuesta)
# Validar si gana
def validarGanador(i):
    if (i==len(jugadores)-1):
        i=0
    # Si saca 21 se planta el juegador y pasamos el turno
    if (jugadores[i].suma_dados==21):
        pasarTurno(i)
    # Si esta plantado y le vuelve a tocar, significa que ya gana
    elif(jugadores[i].turno==True and jugadores[i].planto==True):
        jugadores[i].gana=1
    # Seguimos con el juego
    # Si no gana que siga otra persona
    if (jugadores[i].gana==0): return False
    else: return True
# Tiramos los dados y los turnos quedan de manera ascendente
def comenzarTurno():
    global jugadores
    for i in jugadores:
        menu.mensaje_dado(i.nombre)
        i.dado=generarTiro()
        pintarDados(i.dado,0)
    jugadores=sorted(jugadores, reverse=True)
    jugadores[0].turno=True
    mostrarTodo()
# metodo principal del juego
def main():
    inicio()
    comenzarTurno()
    jugar(0)
    menu.limpiarCache()