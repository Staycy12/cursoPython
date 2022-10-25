## escribir un programa que muestre el eco de todo lo que el usuario
## introduzca hasta que el usuario escriba "salir" que terminara.
contador=5
for num in range(0,contador):
    palabra=input('ingresa algo:')
    if palabra=='salir':
        break
    else:
        contador+=1
    
