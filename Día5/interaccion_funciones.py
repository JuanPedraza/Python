from random import *
from random import shuffle

# Lista inicial
palitos = ['-','--','---','----']

# Mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista

# Pedir al usuario el intento

def intento():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Escriba un número del 1 al 4: ')

    return int(intento)


def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)

    return (dado1,dado2)

# Comprobar intento

def correr_juego(lista, intento):
    if lista[intento-1] == '-':
        print('Has perdido')
    else:
        print('te has salvado')
    print(f'Has selecccionado {lista[intento-1]}')


# Ejecutamos las funciones

palitos_mezclados = mezclar(palitos)
seleccion = intento()
correr_juego(palitos_mezclados,seleccion)