class Bache():

    def __init__(self):
        self.latitud = None
        self.longitud = None
        self.marca_tiempo = None
        self.id = None
        self.direccion = None
        self.metodo = None
        self.sistema_coordenadas = None
        self.precision_gps = None
        self.usuario = None
        self.tipo = None

    def aDiccionario(self):
        return {'latitud': self.latitud, 'longitud': self.longitud, 'marca_tiempo': self.marca_tiempo, 'id': self.id,
                'direccion': self.direccion, 'metodo': self.metodo, 'sistema_coordenadas': self.sistema_coordenadas,
                'precision_gps': self.precision_gps, 'usuario': self.usuario, 'tipo': self.tipo}
