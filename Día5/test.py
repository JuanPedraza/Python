lista_numeros = [2,6,8,4,5,6,9,-10]

def todos_positivos(lista_numeros):

    for numero in lista_numeros:
        print(numero)
        if numero < 0:
            return False
        else:
            pass
    return True

print(todos_positivos(lista_numeros))

lista_numeros = [1,50,90,100,500]


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(0,100):
            suma += numero


    return suma

print(suma_menores(lista_numeros))


