from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
from db_conn.Conexion import Conexion
from procesamiento.ManejadorContrasenas import compararContrasena
#from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode

#Aplicativo
app = Flask(__name__)
#CORS(app)
api = Api(app)

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiJEZXYiLCJjbGllbnRfc2VjcmV0IjoiRGV2UGFzcyJ9.z6N3qREztea2sj35gMMY0LPJBlH8t_k4RbfSDfs-wLo'

#Endpoint para obtener todos los baches

class Baches(Resource):
    def get(self):
        '''
        Obtiene todos los baches de la base de datos

        Output en formato application/json:
        {
            baches: [
                {
                latitud: number,
                longitud: number,
                marca_tiempo: string,
                id: number,
                direccion: string,
                metodo: string,
                sistema_coordenadas: string,
                precision_gps: number,
                usuario: string
                }
            ]
        }
        :return:
            200 code
        '''
        global token

        try:
            code = 200

            token_header = request.headers.get('token')
            if token_header != token:
                code = 401
                raise Exception('Token no valido')

            respuesta = Conexion().obtenerTodosBaches()
            return respuesta, code
        except Exception as e:
            if code == 200:
                code = 500
            return "Error interno del servidor, por favor contacte a soporte, " + str(e), code

    def post(self):
        '''
        Añade un nuevo bache a la base de datos

        Input esperado en formato application/json:
        {
            latitud: number,
            longitud: number,
            direccion: string,
            metodo: string,
            sistema_coordenadas: string,
            precision_gps: number,
            usuario: string
        }
        :return:
            201 code
        '''
        global token

        try:
            code = 201

            content_type = request.headers.get('Content-Type')
            token_header = request.headers.get('token')
            if token_header != token:
                code = 401
                raise Exception('Token no valido')

            if content_type != 'application/json':
                code = 415
                raise Exception('Tipo de body no valido')

            body = request.json

            respuesta = Conexion().crearBache(body)

            return respuesta, code
        except Exception as e:
            if code == 201:
                code = 500
            return "Error interno del servidor, por favor contacte a soporte, " + str(e), code

class Reporte(Resource):
    def post(self, usuarioRecibido):
        '''
        Aumenta en uno la cantidad de reportes generados por el usuario en la base de datos
        /reportes/{usuarioRecibido}

        :return:
            200 code
        '''
        global token

        try:
            code = 200

            token_header = request.headers.get('token')
            if token_header != token:
                code = 401
                raise Exception('Token no valido')

            usuario = usuarioRecibido

            Conexion().aumentarRegistros(usuario)

            respuesta = None

            return respuesta, code
        except Exception as e:
            if code == 201:
                code = 500
            return "Error interno del servidor, por favor contacte a soporte, " + str(e), code

class Usuarios(Resource):
    def post(self, usuarioRecibido):
        '''
        Comprueba si el usuario es válido o no
        /usuarios/{usuarioRecibido}

        Headers contiene contrasena

        Output en formato application/json:
        {
            autorizado: true / false
        }

        :return:
            200 code
        '''

        global token

        try:
            code = 200

            token_header = request.headers.get('token')
            if token_header != token:
                code = 401
                raise Exception('Token no valido')

            usuario = usuarioRecibido
            contrasena = request.headers.get('contrasena')

            contrasenaBd, tipo = Conexion().obtenerContrasenaHashed(usuario)

            if contrasenaBd != None:
                respuesta = compararContrasena(contrasenaBd, contrasena, tipo)
            else:
                respuesta ={'autorizado': False}

            #print(contrasenaBd, contrasena, tipo)


            return respuesta, code
        except Exception as e:
            if code == 201:
                code = 500
            return "Error interno del servidor, por favor contacte a soporte, " + str(e), code


api.add_resource(Baches, '/baches')
api.add_resource(Usuarios, '/usuarios/<string:usuarioRecibido>')
api.add_resource(Reporte, '/reportes/<string:usuarioRecibido>')

