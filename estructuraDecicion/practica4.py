##pedir las 4 notas y evaluar si el promedio es mayor a 13 y mostrar mensaje aprobado caso contrario desaprobado
nota1=int(input("engresa tu 1 nota"))
nota2=int(input("engresa tu 2 nota"))
nota3=int(input("engresa tu 3 nota"))
nota4=int(input("engresa tu 4 nota"))
suma=(nota1+nota2+nota3+nota4)
promedio=(suma/4)
if promedio>13:
    print('estas aprobado')
else:
    print('estas desaprobado')