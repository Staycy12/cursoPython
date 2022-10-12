password= '77822458'
for intentos  in range(1,4):
    print('este es tu',intentos,'intento')
    newPassword=input("ingresa el pasword correcto:")
    if newPassword==password:
        print('bienvenido al sistema joven')
        break
    else:
        print('password incorrecto sigue intentando gil')