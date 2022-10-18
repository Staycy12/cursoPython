##mostrando tabla de multiplicar
eval=True
while eval==True:
    numero =int(input('ingrese el numero de la tabla que decea mostrar:'))
    if numero==0:
     print('error')
     break
    else:
        for numeros in range(1,11):
           print(numeros,'*',numero,'=',numeros*numero)
##if numero1=0:
  ##  for numeros in range(1,11):
    ##     print(numeros,'*',numero,'=',numeros*numero)
##else:
 ##   print('error')
   ## break
