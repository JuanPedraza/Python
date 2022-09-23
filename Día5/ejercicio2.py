def letras_unicas(palabra):
    orden_alfabetico = set()

    for letra in palabra:
        orden_alfabetico.add(letra)

    orden_alfabetico = list(orden_alfabetico)

    orden_alfabetico.sort()

    return orden_alfabetico


print(letras_unicas("entretenido"))
