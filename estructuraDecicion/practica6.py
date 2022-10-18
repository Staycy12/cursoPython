## un chat que se auto responde
mensaje=input('escribe un mensaje:')
if mensaje=='hola':
    print('hola como estas')
    mensaje2=input('dime como te llamas:')
    print('hola',mensaje2,'gusto en conocerte')
    mensaje3=int(input('dime cual es tu edad'))
    if mensaje3>=18:
        print('eres mayor')
    else:
        print('eres menor de edad')
else:
    print('por que no saludas sonsa')