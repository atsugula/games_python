class Jugador:
    # Total de datos de la clase jugador es de 9
    # Parametro self, permite asignar valores a las propiedades de la clase
    def __init__(self, dado, color, turno, nombre, planto, perdidas, tiros_uno , suma_tiros, total_tiros, dinero_inicia):
        self.dado=dado
        self.color=color
        self.turno=turno
        self.nombre=nombre
        self.planto=planto
        self.perdidas=perdidas
        self.tiros_uno=tiros_uno
        self.suma_tiros=suma_tiros
        self.total_tiros=total_tiros
        self.dinero_inicia=dinero_inicia