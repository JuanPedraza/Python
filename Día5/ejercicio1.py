def devolver_distintos(a,b,c):
    lista = [a, b, c]
    suma = a + b + c

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos(12, 4, 6))

