#Calculadora ***
import time

print("¡Hola! Bienvenido a la calculadora escrita en Python y desarrollada por mi")
time.sleep(1)
print(f"Ahora sí, comencemos: ")
time.sleep(0.8)

numero1 = int(input("Dime el primer número: "))
numero2 = int(input(f"Bien! Ahora dime el segundo número: "))
print(f"De acuerdo, has escogido el {numero1} y el {numero2}")
time.sleep(1)

simbolo = input(f"¿Qué quieres hacer con estos números? (Escribe la primera letra)\n -Sumar\n -Restar\n -Multiplicar\n -Dividir\n")

if simbolo == 's' or simbolo == "S":
    print(f"{numero1} + {numero2} =",(numero1+numero2))
elif simbolo == 'r' or simbolo == "R":
    print(f"{numero1} - {numero2} =",(numero1-numero2))
elif simbolo == 'm' or simbolo == "M":
    print(f"{numero1} * {numero2} =",(numero1*numero2))
elif simbolo == 'd' or simbolo == "D":
    print(f"{numero1} / {numero2} =",(numero1/numero2))
else:
    print(f"No has escrito ninguna letra correcta\nS|s para sumar R|r para restar M|m para multiplicar o D|d para dividir")