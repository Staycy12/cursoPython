##esta estructura realiza una accion especifica
##if/else  si/sino
##elif   seleccion multiple
pasword='77822458'
condicion=true
intentos=1
while condicion==true:
    print('este es tu',intentos,'intentos')
    newPassword=input('ingresa el password correcto:')
    if newPassword==password:
        print('bienvenido al sistema joven ilustre')
        condicion=False
    else:
        print('eres un gil')
        intentos+=1