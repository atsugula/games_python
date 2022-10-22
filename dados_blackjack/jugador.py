class Jugador:
    # Total de datos de la clase jugador es de 9
    # Parametro self, permite asignar valores a las propiedades de la clase
    def __init__(self, dado, gana, color, turno, nombre, planto, perdio, tiros_uno , suma_dados, total_tiros, dinero_inicia):
        self.dado=dado
        self.gana=gana
        self.color=color
        self.turno=turno
        self.nombre=nombre
        self.planto=planto
        self.perdio=perdio
        self.tiros_uno=tiros_uno
        self.suma_dados=suma_dados
        self.total_tiros=total_tiros
        self.dinero_inicia=dinero_inicia
    def __gt__(self, jugador):
        return self.dado > jugador.dado