#upper=(mayusculas)
## por consola la suma de 4+5

def mensaje(nombre,apellido,accion):
    if accion == 'saludo':
        mensaje='hola',nombre,apellido,'como estas'
    elif accion=='despedida':
        mensaje='adios ',nombre,apellido
    return mensaje
respuesta=mensaje('jose','alvarez','despedida')
print(respuesta)