#hacer una FUNCION que me retorne los numeros fibonacci
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in range(10):
    print(rec_fib(i))

#crear una funcion que me retorne el factorial de un numero n




# crear una funcion que me diga si una palabra es polindronos