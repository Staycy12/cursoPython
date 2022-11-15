#4.siempre la funcion tiene que retornar un tipo de dato
def saludo(nombre):
    respuesta=f'hola como estas {nombre}'
    return respuesta
#como uso
arrayAmigos=['ronald','claudio','diego','jose','mozita','kevin','lilian']
for amigo in range(0,len(arrayAmigos)):
    print(saludo(arrayAmigos[amigo]))
