##si es entre 13 y 15 == regular
##si entre 15 y 17 == bueno
##si entre 17 y 20 === excelente
nota1=float(input("engresa tu 1 nota"))
nota2=float(input("engresa tu 2 nota"))
nota3=float(input("engresa tu 3 nota"))
nota4=float(input("engresa tu 4 nota"))
promedio=(nota1+nota2+nota3+nota4)/4

print(promedio)
if promedio<13:
    print('eres burro')
if promedio>13 and promedio<=15:
    print('regular')
if promedio>15 and promedio<=17:
    print('bueno')
if promedio>17 and promedio<=20:
    print('excelente')
