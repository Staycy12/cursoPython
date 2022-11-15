vocalesUno=['a','e']
vocalesDos=['i','o','u']
vocalesUno.extend(vocalesDos)
vocalesUno[3]='00'
vocalesUno.remove('u')
print(vocalesUno)