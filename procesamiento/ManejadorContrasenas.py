import bcrypt

def encriptar(clave):
    salt = bcrypt.gensalt()
    clave = clave.encode('utf-8')
    clave = bcrypt.hashpw(clave, salt)
    return clave

def compararContrasena(encriptada, ingresada, tipo):
    encriptada = encriptada[2:-1]
    valido = encriptada.encode('utf-8') == bcrypt.hashpw(ingresada.encode('utf-8'), encriptada.encode('utf-8'))
    respuesta = {'autorizado': valido}
    if valido:
        respuesta = {'autorizado': valido, 'tipo': tipo}
    return respuesta