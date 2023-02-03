import mysql.connector
from mysql.connector import errorcode
from .ProcesadorBD import ProcesadorBD


class Conexion():

    def __init__(self):
        pass

    def obtenerTodosBaches(self):
        try:
            conexion = mysql.connector.connect(user='', password='',
                                               host='darvaron14.mysql.pythonanywhere-services.com',
                                               database='darvaron14$proyectoGrado')
            cursor = conexion.cursor()

            query = ('SELECT Bache.*, Tipo_Usuario.tipo FROM Bache, Tipo_Usuario, Usuario  WHERE Tipo_Usuario.tipo_id=Usuario.tipo_id AND Bache.usuario=Usuario.usuario')

            cursor.execute(query, ())

            respuesta = ProcesadorBD().procesarBaches(cursor)

            # print(respuesta)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Autenticacion incorrecta")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)
        else:
            cursor.close()
            conexion.close()
            return respuesta

    def crearBache(self, body):
        try:

            bache = ProcesadorBD().setBacheConBody(body)

            conexion = mysql.connector.connect(user='', password='',
                                               host='darvaron14.mysql.pythonanywhere-services.com',
                                               database='darvaron14$proyectoGrado')
            cursor = conexion.cursor()

            query = (
                'INSERT INTO Bache (latitud, longitud, direccion, metodo, sistema_coordenadas, precision_gps, usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)')
            valores = (
            float(bache.latitud), float(bache.longitud), bache.direccion, bache.metodo, bache.sistema_coordenadas,
            float(bache.precision_gps), bache.usuario)

            cursor.execute(query, valores)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Autenticacion incorrecta")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)
        else:
            conexion.commit()
            cursor.close()
            conexion.close()
            return None

    def obtenerContrasenaHashed(self, usuario):
        try:
            conexion = mysql.connector.connect(user='', password='',
                                               host='darvaron14.mysql.pythonanywhere-services.com',
                                               database='darvaron14$proyectoGrado')
            cursor = conexion.cursor()

            query = ('SELECT Usuario.contrasena, Tipo_Usuario.tipo FROM Usuario, Tipo_Usuario WHERE Usuario.usuario=%s AND Usuario.tipo_id=Tipo_Usuario.tipo_id')
            valores = (usuario, )

            cursor.execute(query, valores)

            registros = cursor.fetchall()
            registrosObtenidos = len(registros)

            contrasenaOb = None
            tipo = None
            if registrosObtenidos == 0:
                print("Usuario no encontrado")
            else:
                print("Usuario encontrado")
                for (contrasena, tipo) in registros:

                    contrasenaOb = contrasena
                    tipo = tipo
                    break

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Autenticacion incorrecta")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)
        else:
            conexion.commit()
            cursor.close()
            conexion.close()
            return contrasenaOb, tipo

    def aumentarRegistros(self, usuario):
        try:
            conexion = mysql.connector.connect(user='', password='',
                                               host='darvaron14.mysql.pythonanywhere-services.com',
                                               database='darvaron14$proyectoGrado')
            cursor = conexion.cursor()

            query = ('UPDATE Consolidado SET conteoRegistros = conteoRegistros + 1 WHERE usuario=%s')
            valores = (usuario, )

            cursor.execute(query, valores)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Autenticacion incorrecta")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)
        else:
            conexion.commit()
            cursor.close()
            conexion.close()
            return None

