import json
from .Bache import Bache


class ProcesadorBD():

    def __init__(self):
        pass

    def procesarBaches(self, cursor):
        respuesta = {}
        baches = []
        for (latitud, longitud, marca_tiempo, id, direccion, metodo, sistema_coordenadas, precision_gps, usuario, tipo) in cursor:
            bache = Bache()

            bache.latitud = str(latitud)
            bache.longitud = str(longitud)
            bache.marca_tiempo = str(marca_tiempo)
            bache.id = str(id)
            bache.direccion = direccion
            bache.metodo = metodo
            bache.sistema_coordenadas = sistema_coordenadas
            bache.precision_gps = str(precision_gps)
            bache.usuario = usuario
            bache.tipo = tipo

            baches.append(bache.aDiccionario())

        respuesta['baches'] = baches
        return respuesta

    def setBacheConBody(self, body):
        bache = Bache()

        bache.latitud = body['latitud']
        bache.longitud = body['longitud']
        bache.direccion = body['direccion']
        bache.metodo = body['metodo']
        bache.sistema_coordenadas = body['sistema_coordenadas']
        bache.precision_gps = body['precision_gps']
        bache.usuario = body['usuario']

        return bache
