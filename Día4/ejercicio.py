# from random import *
#
# name = input('Digita tu nombre: ')
# intentos = 8
#
# aleatorio = randint(1,100)
# while intentos > 0:
#     number = int(input('Escoge un número entre el 1 y el 100: '))
#     if number == aleatorio:
#         print(f"Adivinaste, el número escogido fue {number} coincide con {aleatorio} ")
#     elif number != aleatorio:
#         intentos -= 1
#         number = int(input(f'Te quedan {intentos} '))
#     else:
#         print('Lo sentimos, no te quedan más intentos')
#
from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")