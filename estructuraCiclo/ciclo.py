##int tipo de texto a un dato de tipo numerico real o entero
 ## input metodo de python que pide un dato por consola al ususario
condicion=True
while condicion==True:
    numero=int(input('ingresa el num ganador'))
    if numero==10:
      print('ganaste el premio')
      condicion=False
    else:
        print('sientate chato ese es el numero')