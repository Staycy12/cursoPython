# precios = [50, 75, 46, 22, 80, 65, 8]
# min = max = precios[0]
# for precios in precios:
#     if precios < min:
#         min = precios
#     elif precios > max:
#         max = precios
# print("El mínimo es " + str(min)) 
# print("El máximo es " + str(max))

# mayor=["hoal","como estas", "jose ees un chage"] 
# min=max=mayor[0]
# for lilian in mayor:
#      if lilian < min:
#          min = lilian
#      elif lilian > max:
#          max = lilian
# print("El mínimo es " + str(min)) 
# print("El máximo es " + str(max))

def mas_larga(lista):
	palabra_mayor = len(lista[0])
	palabra_mostrar = lista[0]

	for palabra in lista:
		if palabra_mayor <= len(palabra):
			palabra_mostrar = palabra
			palabra_mayor = len(palabra)
		else:
			palabra_mostrar = palabra_mostrar

	print(palabra_mostrar)


lista = ["hola", "hola jose", "hola jose chage"]
mas_larga(lista)

# def creador_dict(cadena):
#   '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
#   lista_1= cadena.split()
#   dict_1={}
#   for i in list_1:
#     if i in dict_1:
#       dict_1[i] +=1
#     else:
#       dict_1[i]= 1
#   return dict_1

# def contador_dict(dictionario):
#   '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
#   palabra_frecuente= ''
#   cantidad=0
#   for keys,values in dictionario.items():
#     if values > cantidad:
#       cantidad= values
#       palabra_frecuente= keys
#   return palabra_frecuente,cantidad
# entrada=input('Ingrese su cadena de caracteres: ')
# print(creador_dict(entrada))
# print(contador_dict(creador_dict(entrada)))