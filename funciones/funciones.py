##funciones
##2tipos de funciones
##funciones propias de paython
print(parametros) ##sirve para mostrar mensajes o resultados
int()## esta funcion sirve para convertir string en entero
input()##esta funcion sirve para pedir datos el usuario

##todo lo que se ingrese en input sera tomado como texto

##funciones creadas
##creando funciones hola
def suma(a,b):
    resultado=a+b
    return "hola"

##uso de funcion
print(suma(4,6))
#def

#4.siempre la funcion tiene que retornar un tipo de dato
def saludo(nombre):
    respuesta=f'hola como estas {nombre}'
    return respuesta
#como uso
arrayAmigos=['ronald','claudio','diego','jose','mozita','kevin','lilian']
for amigo in range(0,len(arrayAmigos)):
    print(saludo(amigo))
 


