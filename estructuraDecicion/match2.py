##tendremos una variable con el mensaje hola mundo
##pedir al usuario un texto
##si el texto ingresado es hola(mostraras el mensaje completo)
##si el texto ingresado es como estas(extraeras del mensaje la palabra hola)
##si el texto ingresado es como saludos(extraeras del mensaje la palabra mundo)
##si se ingresa otro texto
##mostraras por efecto el mensaje de error
from ctypes.wintypes import HLOCAL


mensaje='hola mundo'
texto=input("engresa un texto:")
match texto:
    case 'hola':
        print(mensaje[:])
    case 'como estas':
        print(mensaje[:])
    case 'saludos':
        print(mensaje[:])
    case _:
        print('error')
        
