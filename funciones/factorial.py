#crear una funcion que me retorne el factorial de un numero n
def factorial(n): 
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return resultado