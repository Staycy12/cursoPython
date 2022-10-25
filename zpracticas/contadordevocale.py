##contador de vocales
#oracion=input('ingrese su oracion')
#vocales=['a','e','i','o','u']
#contadorvocales=0
#for letras in oracion:
#    if letras in vocales:
#        contadorvocales+=1
#print('la cantidad de vocales:',contadorvocales)
sentence =input('ingresa una oracion:')
handlerVocals=0
for word in sentence:
    match word:
        case 'a':
           handlerVocals+1
        case 'e':
           handlerVocals+1
        case 'i':
           handlerVocals+1
        case 'o':
            handlerVocals+1
        case 'u':
            handlerVocals+1
            print('la cantidad de vocales es:',handlerVocals)
            